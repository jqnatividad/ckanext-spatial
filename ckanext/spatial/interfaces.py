from ckan.plugins.interfaces import Interface


class ISpatialHarvester(Interface):

    def get_package_dict(self, context, data_dict):
        '''
        Allows to modify the dataset dict that will be created or updated

        This is the dict that the harvesters will pass to the `package_create`
        or `package_update` actions. Extensions can modify it to suit their
        needs, adding or removing filds, modifying the default ones, etc.

        This method should always return a package_dict. Note that, although
        unlikely in a particular instance, this method could be implemented by
        more than one plugin.


        :param context: Contains a reference to the model, eg to
                        perform DB queries
        :type context: dict
        :param data_dict: Available data. Contains three keys:

            * `package_dict`
               The default package_dict generated by the harvester. Modify this
               or create a brand new one.
            * `iso_values`
               The parsed ISO XML document values. These contain more fields
               that are not added by default to the ``package_dict``.
            * `harvest_object`
               A ``HarvestObject`` domain object which contains a reference
               to the original metadata document (``harvest_object.content``)
               and the harvest source (``harvest_object.source``).

        :type data_dict: dict

        :returns: A dataset dict ready to be used by ``package_create`` or
                  ``package_update``
        :rtype: dict
        '''
        return data_dict['package_dict']

    def transform_to_iso(self, original_document, original_format, harvest_object):
        '''
        Transforms an XML document to ISO 19139

        This method will be only called from the import stage if the
        harvest_object content is null and original_document and
        original_format harvest object extras exist (eg if an FGDC document
        was harvested).

        In that case, this method should do the necessary to provide an
        ISO 1939 like document, otherwise the import process will stop.


        :param original_document: Original XML document
        :type original_document: string
        :param original_format: Original format (eg 'fgdc')
        :type original_format: string
        :param harvest_object: HarvestObject domain object (with access to
            job and source objects)
        :type harvest_object: HarvestObject

        :returns: An ISO 19139 document or None if the transformation was not
            successful
        :rtype: string

        '''
        return None

