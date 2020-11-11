from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string, get_yields


class SimplyWhisked(AbstractScraper):
    @classmethod
    def host(cls):
        return "simplywhisked.com"

    def title(self):
        return self.schema.title()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        return self.schema.instructions()

    def ratings(self):
        return self.schema.ratings()
