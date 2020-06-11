from fitparse import FitFile

fitfile = FitFile('./data/Test1.fit')
# Get all data messages that are of type record
print "[{"
for record in fitfile.get_messages('record'):

    # Go through all the data entries in this record
    for record_data in record:

        # Print the records name and value (and units if it has any)
        if False: #record_data.units:
            print "%s: %s %s" % (
                record_data.name, record_data.value, record_data.units,
            )
        else:
            print "  \"%s\": \"%s\"," % (record_data.name, record_data.value)
    print "}, {"
print "}]"
