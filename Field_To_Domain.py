import arcpy
def Field_To_Domain(gdb, fc, field, domain_name):
    # set the environment
    arcpy.env.workspace = gdb
    # Check if the domain already exists
    all_domains = [x.name for x in arcpy.da.ListDomains(gdb)]
    if  domain_name in all_domains:
        print(f"The domain {domain_name} already exists.")
        arcpy.AddError(f"The domain {domain_name} already exists.")
        return
    
    # Determine field type
    fields = arcpy.ListFields(fc)
    field_obj = next((f for f in fields if f.name == field), None)
    if not field_obj:
        print(f"Field '{field}' not found in the feature class.")
        arcpy.AddError(f"Field '{field}' not found in the feature class.")
        return
    field_type = field_obj.type
    # Create the domain based on field type
    if field_type in ['String', 'Date']:
        arcpy.management.CreateDomain(gdb, domain_name, domain_name, "TEXT", 'CODED')
    elif field_type in ['Double', 'Single', 'Integer']:
        arcpy.management.CreateDomain(gdb, domain_name, domain_name, "LONG", 'CODED')
    elif field_type == 'Short':
        arcpy.management.CreateDomain(gdb, domain_name, domain_name, "SHORT", 'CODED')
    elif field_type == 'Float':
        arcpy.management.CreateDomain(gdb, domain_name, domain_name, "FLOAT", 'CODED')
    elif field_type in ['GUID', 'GlobalID']:
        arcpy.management.CreateDomain(gdb, domain_name, domain_name, "GUID", 'CODED')
    else:
        print(f"Invalid field type '{field_type}'. Domain cannot be created.")
        arcpy.AddError(f"Invalid field type '{field_type}'. Domain cannot be created.")
        return
    # get sorted unique values from the target field
    all_values = [row[0] for row in  arcpy.da.SearchCursor(fc, [field]) if row[0]]
    unique_values = sorted(list(set(all_values)))
    if not unique_values:
        arcpy.AddError(f"Field :{field} in FeatureClass :{fc} hase no values")
        return
    # assign the field unique value to the domain
    for code, desc in enumerate(unique_values,1):
        arcpy.management.AddCodedValueToDomain(gdb, domain_name, code, code_description=desc)
    # assign the domain to the target field
    arcpy.management.AssignDomainToField(fc, field, domain_name)
    # update the existing value to the domain code value
    with arcpy.da.UpdateCursor(fc, [field]) as cursor:
        for row in cursor:
            for c, d in enumerate(unique_values,1):
                if row[0] == d:
                    row[0] = c
            cursor.updateRow(row)
        print("All Done Pro")
        
if __name__ == '__main__':
    # ScriptTool parameters
    gdb = arcpy.GetParameterAsText(0)
    fc = arcpy.GetParameterAsText(1)
    field = arcpy.GetParameterAsText(2)
    domain_name = arcpy.GetParameterAsText(3)
    
    # Run the Function
    Field_To_Domain(gdb, fc, field, domain_name)
    
