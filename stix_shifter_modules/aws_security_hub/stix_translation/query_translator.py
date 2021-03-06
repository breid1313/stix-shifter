from stix_shifter_utils.modules.base.stix_translation.base_query_translator import BaseQueryTranslator
from . import query_constructor


class QueryTranslator(BaseQueryTranslator):

    def map_field(self, stix_object_name, stix_property_name):
        if stix_object_name in self.map_data and stix_property_name in self.map_data[stix_object_name]["fields"]:
            return self.map_data[stix_object_name]["fields"][stix_property_name]
        else:
            return []

    def transform_antlr(self, data, antlr_parsing_object):

        query_string = query_constructor.translate_pattern(
            antlr_parsing_object, self)
        return query_string
