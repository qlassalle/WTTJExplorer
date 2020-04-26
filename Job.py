class Job:
    name = ''
    published_at = ''
    organization_name = ''
    organization_size = 0
    contract_type = ''
    url = ''
    location = ''

    def __init__(self, name, published_at, organzation_name, organization_size, contract_type, slug, location) -> None:
        super().__init__()
        self.name = name
        self.published_at = published_at
        self.organization_name = organzation_name
        self.organization_size = organization_size
        self.contract_type = contract_type
        self.url = f"https://www.welcometothejungle.com/fr/companies/{self.company_name_as_url()}/jobs/{slug}"
        self.location = location

    def company_name_as_url(self):
        return str.lower(self.organization_name).replace(" ", "_")


    # def __str__(self) -> str:
    #     # return 'slug : ' + self.slug + ' name : ' + self.name + ' published_at : ' + self.published_at +
    #     return f"name: {self.name},  published_at: {self.published_at}, company: {self.organization_name}, " \
    #            f"size: {self.organization_size}, contract: {self.contract_type}"
