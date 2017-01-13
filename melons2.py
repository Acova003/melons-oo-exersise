"""This file should have our order classes in it."""


class AbstractMelonOrder(object):
    """ You fill in the rest """

    def get_total(self):
        """Calculate price."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price
        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True

    def __init__(self, species, qty, country_code="USA"):
        """Initialize melon order attributes"""

        self.species = species
        self.qty = qty
        self.shipped = False


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    def __init__(self, species, qty):
        super(DomesticMelonOrder, self).__init__(species, qty)
        self.tax()
        self.country_code = "USA"

    def tax(self):
        """Initialize melon order attributes"""

        self.order_type = "domestic"
        self.tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, country_code, species, qty):
        super(InternationalMelonOrder, self).__init__(species, qty)
        self.country_code = country_code
        self.tax()

    def tax(self):
        """Initialize melon order attributes"""

        self.order_type = "international"
        self.tax = 0.17

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
