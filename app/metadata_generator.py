import random
import logging
import json


class MetadataGenerator:
    def __init__(
        self,
        nft_number: int = 100,
        metadata_path: str = "./metadata",
        rarity_path: str = "./rarity.json",
        project_name: str = "",
        project_description: str = "",
        project_images_link: str = "",
    ):
        """
        Read rarity.json file
        :param nft_number: number of nfts
        :param metadata_path: path to metadata folder
        :param rarity_path: path to rarity.json file
        :param project_name: project name
        :param project_description: project description
        :param project_images_link: project images link
        :return: rarity.json file
        """
        try:
            self.logger: logging = logging.getLogger()
            self.logger.setLevel(logging.DEBUG)

            self.project_name: str = project_name
            self.project_description: str = project_description
            self.project_images_link: str = project_images_link

            self.nft_number: int = nft_number
            self.metadata_path: str = metadata_path
            self.rarity_path: str = rarity_path
            self.rarities: dict = self.read_rarity()
            self.generated_metadata: list = list()

            self.logger.info("MetadataGenerator initialized.")

        except Exception as e:
            self.logger.error(e)
            print(e)
            return e

    def read_rarity(self) -> dict:
        """
        Read rarity from rarity.json
        :return: rarity
        """
        try:
            self.logger.info("Reading rarity.json file.")
            with open(self.rarity_path) as f:
                return json.load(f)

        except Exception as e:
            self.logger.error(e)
            print(e)
            return e

    def generate_unique_metadata(self) -> list:
        """
        Generate a unique metadata
        :return: list of a unique metadata that does not exist in generated_metadata
        """
        try:
            self.logger.info("Generating unique metadata.")
            current_metadata: list = list()

            for i in range(len(self.rarities)):
                current_trait = list(self.rarities.keys())[i]
                current_trait_keys = list(self.rarities[current_trait].keys())
                current_trait_values = list(self.rarities[current_trait].values())

                current_metadata.append(
                    random.choices(current_trait_keys, weights=current_trait_values)[0]
                )

            if current_metadata not in self.generated_metadata:
                self.logger.info("Unique metadata generated.")
                self.generated_metadata.append(current_metadata)

                return current_metadata
            else:
                self.logger.info("Metadata already exists. Generating new metadata.")

                return self.generate_unique_metadata()

        except Exception as e:
            self.logger.error(e)
            print(e)
            return e

    def write_metadata(self, metadata: list, nft_number: int) -> bool:
        """
        Write metadata to metadata folder
        :param metadata: metadata to write
        :return: bool (true if success / false if failed)
        """
        try:
            self.logger.info("Writing metadata to metadata folder.")

            final_metadata = {
                "name": f"{self.project_name} #{nft_number}",
                "description": self.project_description,
                "image": f"{self.project_images_link}/{nft_number}.png",
                "attributes": [
                    {
                        "trait_type": list(self.rarities.keys())[i],
                        "value": str(metadata[i]),
                    }
                    for i in range(len(metadata))
                ],
            }

            with open(f"./metadata/{nft_number}.json", "w") as f:
                self.logger.info("Writing Metadata to metadata folder...")
                json.dump(final_metadata, f)

            return True

        except Exception as e:
            self.logger.error(e)
            print(e)
            return False

    def generate_all_and_write(self):
        """
        Generate all metadata and write to metadata folder
        :return: bool (true if success / false if failed)
        """
        try:
            self.logger.info("Generating all metadata and writing to metadata folder.")
            for i in range(1, self.nft_number + 1):
                self.write_metadata(self.generate_unique_metadata(), i)

            return True

        except Exception as e:
            self.logger.error(e)
            print(e)
            return False


if __name__ == "__main__":
    metadata_generator = MetadataGenerator(
        project_name="Test",
        project_description="Test",
        project_images_link="https://test.com",
        nft_number=50
    )

    metadata_generator.generate_all_and_write()
