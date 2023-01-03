import os
import json
import logging
from PIL import Image


class NFTGenerator:
    def __init__(
        self,
        nft_number: int = 100,
        images_path: str = "./images",
        metadata_path: str = "./metadata",
        image_extension: str = "png",
    ) -> None:
        """
        Initialize NFTGenerator.
        :param nft_number: Number of NFTs to generate.
        :param images_path: Path to images.
        :param metadata_path: Path to metadata.
        :param image_extension: Image extension.
        :return: None.
        """
        try:
            self.logger: logging = logging.getLogger()
            self.logger.setLevel(logging.DEBUG)

            self.nft_number: int = nft_number
            self.metadata_path: str = metadata_path
            self.images_path: str = images_path
            self.image_extension: str = image_extension

            self.logger.info("NFTGenerator initialized.")

        except Exception as e:
            self.logger.error(e)
            print(e)
            return e

    def read_metadata(self, nft_number: int = 0) -> dict:
        """
        Read metadata.
        :param nft_number: NFT number.
        :return: Metadata.
        """
        try:
            self.logger.info("Reading metadata.json file.")
            with open(f"{self.metadata_path}/{nft_number}.json") as f:
                return json.load(f)

        except Exception as e:
            self.logger.error(e)
            print(e)
            return e

    def generate_nft(self, nft_number: int = 0) -> None:
        """
        Generate NFT.
        :param nft_number: NFT number.
        :return: NFT.
        """
        try:
            self.logger.info(f"Generating NFT #{nft_number}")
            metadata: dict = self.read_metadata(nft_number=nft_number)

            background = Image.open(
                f"{self.images_path}/"
                f'{metadata["attributes"][0]["trait_type"]}/'
                f'{metadata["attributes"][0]["value"]}.{self.image_extension}'
            )

            for i in range(1, len(metadata["attributes"])):
                foreground = Image.open(
                    f"{self.images_path}/"
                    f'{metadata["attributes"][i]["trait_type"]}/'
                    f'{metadata["attributes"][i]["value"]}.{self.image_extension}'
                )
                background.paste(foreground, (0, 0), foreground)

            background.save(
                f"./nfts/{nft_number}.{self.image_extension}",
                "PNG",
                quality=100,
                optimize=True,
                progressive=True,
            )

        except Exception as e:
            self.logger.error(e)
            print(e)
            return e

    def generate_all(self) -> bool:
        """
        Generate all NFTs.
        :return: True if all NFTs are generated.
        """
        try:
            self.logger.info("Generating all NFTs...")
            for i in range(1, self.nft_number + 1):
                self.generate_nft(nft_number=i)
            self.logger.info("All NFTs generated.")

            return True

        except Exception as e:
            self.logger.error(e)
            print(e)
            return False
