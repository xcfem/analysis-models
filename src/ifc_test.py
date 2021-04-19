from __future__ import print_function

import ifcopenshell

ifc_file= ifcopenshell.open('./Sculpture.ifc')

products = ifc_file.by_type('IfcProduct')
for product in products:
    isA= product.is_a()
    if(isA=='IfcFastener'):
        #print(str(product.GlobalId), str(product.Name))
        for definition in product.IsDefinedBy:
            if definition.is_a('IfcRelDefinesByProperties'):
                    property_set = definition.RelatingPropertyDefinition
                    print(property_set.Name) # Might return Pset_WallCommon
