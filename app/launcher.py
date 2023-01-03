from metadata_generator import MetadataGenerator
from nft_generator import NFTGenerator


if __name__ == "__main__":
    project_name = "My Project"
    project_description = "My Project Description"
    project_image = "https://myproject.com/image.png"
    nft_number = 25

    # Generating and saving metadata
    metadata_generator = MetadataGenerator(
        project_name=project_name,
        project_description=project_description,
        project_images_link=project_image,
        nft_number=nft_number,
    )
    metadata_generator.generate_all_and_write()

    # Generating and saving NFTs
    nft_generator = NFTGenerator(nft_number=nft_number)
    nft_generator.generate_all()
