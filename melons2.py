"""This file should have our order classes in it."""


class AbstractMelonOrder(object):
    """ You fill in the rest """

    def get_total(self):
        """Calculate price."""

        if self.species == "Christmas melons":
            base_price = round(5 * 1.5)
        else:
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
    
    order_type = "domestic"
    tax = 0.08
    country_code = "USA"

    def __init__(self, species, qty):
        super(DomesticMelonOrder, self).__init__(species, qty)


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    
    order_type = "international"
    tax = 0.17
    fee = 3

    def __init__(self, country_code, species, qty):
        super(InternationalMelonOrder, self).__init__(species, qty)
        self.country_code = country_code


    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    def get_total(self):
        total = super(InternationalMelonOrder, self).get_total()
        if self.qty < 10:
            total += self.fee  # refers to class attribute using self
        
        return total
