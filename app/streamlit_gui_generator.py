import io
import os
import json

import streamlit as st
from PIL import Image

from metadata_generator import MetadataGenerator
from nft_generator import NFTGenerator


st.set_page_config(layout="wide", page_title="NFT and Metadata Generator")
st.markdown(
    "<h1 style='text-align: center'>NFT and Metadata " "Generator</h1>",
    unsafe_allow_html=True,
)

st.sidebar.write("# Project Information")

project_name = st.sidebar.text_input("Project Name", "My Project Name")
project_description = st.sidebar.text_area(
    "Project Description", "My Project Description"
)
project_images_link = st.sidebar.text_input(
    "Project Image Link", "https://myproject.com"
)
nft_number = st.sidebar.number_input("Number of NFTs", 1, 100000, 1)
image_extension = st.sidebar.selectbox(
    "Choose an image extension",
    ("png", "jpg", "jpeg"),
    index=0,
)  # index=0 is the default value (.png)


layer_number = st.sidebar.number_input("Number of layers", 0, 1000, 0)

if layer_number > 0:
    layer_names: list = []
    trait_category_keys: list = []
    trait_category_probabilities: list = []
    images: dict = {}

    for i in range(layer_number):

        layer_name = st.text_input(
            f"Layer {i + 1} name (the folders will be " f"renamed accordingly):",
            f"Layer" f" {i + 1} name",
        )
        layer_names.append(layer_name)

        trait_category_key = st.text_input(
            f"Trait category {i + 1} names (separated " f"by semicolon; no spaces):",
            f"Name 1;Name 2;Name 3",
        )
        trait_category_keys.append(trait_category_key)

        trait_category_probability = st.text_input(
            f"Trait category {i + 1} probability (separated "
            f"by semicolon; no spaces):",
            f"100;500;800",
        )
        trait_category_probabilities.append(trait_category_probability)

        image = st.file_uploader(
            f"Please drag the images for the {layer_name} trait:",
            type=[f"{image_extension}"],
            help="Please drag the images for the trait.",
            accept_multiple_files=True,
            key=i,
        )
        images[layer_name] = image

        print(" ")

        print(trait_category_keys)
        print(trait_category_probabilities)
        print(layer_names)
        print(images)

        st.markdown("---")


def generate_rarity_st():
    rarity = {}
    for z in range(layer_number):
        keys_list: list = trait_category_keys[z].split(";")
        traits_list: list = [
            float(z) for z in trait_category_probabilities[z].split(";")
        ]
        rarity[layer_names[z]] = dict(zip(keys_list, traits_list))

    with open(f"./rarity.json", "w") as f:
        json.dump(rarity, f)

    st.sidebar.success("Rarity file generated and saved in the current directory.")

    metadata_generator = MetadataGenerator(
        project_name=project_name,
        project_description=project_description,
        project_images_link=project_images_link,
        nft_number=nft_number,
    )
    metadata_generator.generate_all_and_write()

    st.sidebar.success(
        "Metadata files were generated and saved in the metadata/ folder."
    )

    return rarity


def generate_nfts_st():
    try:
        # Creating the according directories
        for x in range(layer_number):
            os.mkdir(f"./images/{layer_names[x]}")
        st.sidebar.success("Directories created.")

        # Saving the images in the directories
        for y in range(len(list(images.keys()))):
            for uploaded_image in images[list(images.keys())[y]]:
                bytes_data = uploaded_image.read()
                current_image = Image.open(io.BytesIO(bytes_data))
                current_image.save(
                    f"./images/{list(images.keys())[y]}/" f"{uploaded_image.name}"
                )
        st.sidebar.success("Images saved in the directories.")

        # Call the generate function
        with st.spinner():
            nft_generator = NFTGenerator(nft_number=nft_number)
            nft_generator.generate_all()
        st.balloons()
        st.sidebar.success("NFTs were generated and saved in the current directory")

    except Exception as e:
        st.sidebar.error(f"Error: {e}")


col1, col2 = st.sidebar.columns(2)
try:
    if col1.button("Generate Metadata"):
        if layer_number == 0:
            st.sidebar.error("Add some layers first!")
        else:
            generate_rarity_st()
            st.snow()
            st.sidebar.info("You can now generate Generate NFTs with the button.")
except Exception as e:
    st.sidebar.error(e)

try:
    if col2.button("Generate NFTs"):
        if layer_number == 0:
            st.sidebar.error("Add some layers first!")
        else:
            generate_nfts_st()
except Exception as e:
    st.sidebar.error(e)

# Copyright images
st.sidebar.image("../src/medipolchain.png", use_column_width=True)
st.sidebar.markdown(
    "<h4 style='text-align: center;'>Made with ❤️ by "
    "<a href='https://twitter.com/medipolchain'>Medipol "
    "Blockchain Community</a></h4>",
    unsafe_allow_html=True,
)
