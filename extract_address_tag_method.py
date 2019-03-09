import csvkit
import usaddress

# expected format in input.csv: first column 'id', second column 'address'
with open('input.csv', 'r') as f:
    reader = csvkit.DictReader(f)

    all_rows = []
    for row in reader:
        try:
            parsed_addr = usaddress.tag(row['address'])
            row_dict = parsed_addr[0]
        except:
            row_dict = {'error':'True'}

        row_dict['id'] = row['id']
        all_rows.append(row_dict)

field_list = ['id','AddressNumber', 'AddressNumberPrefix', 'AddressNumberSuffix', 'BuildingName', 
              'CornerOf','IntersectionSeparator','LandmarkName','NotAddress','OccupancyType',
              'OccupancyIdentifier','PlaceName','Recipient','StateName','StreetName',
              'StreetNamePreDirectional','StreetNamePreModifier','StreetNamePreType',
              'StreetNamePostDirectional','StreetNamePostModifier','StreetNamePostType',
              'SubaddressIdentifier','SubaddressType','USPSBoxGroupID','USPSBoxGroupType',
              'USPSBoxID','USPSBoxType','ZipCode', 'error']

with open('output.csv', 'wb') as outfile:
    writer = csvkit.DictWriter(outfile, field_list)
    writer.writeheader()
    writer.writerows(all_rows)