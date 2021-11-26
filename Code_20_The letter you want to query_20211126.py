text = """ArcGIS Pro, the powerful single desktop GIS application, is a feature-packed software developed
 with enhancements and ideas from the ArcGIS Pro user community. ArcGIS Pro supports data visualization; advanced analysis;
  and authoritative data maintenance in 2D, 3D, and 4D. It supports data sharing across a suite of ArcGIS 
  products such as ArcGIS Online and ArcGIS Enterprise, and enables users to work across 
  the ArcGIS system through Web GIS. Discover the full spectrum of tools and capabilities within ArcGIS Pro today."""

letter = input("The letter you want to query: ")

numb = ''
#The beginning of the number of letters
for s in text:
    if letter == s:
        numb += letter
    
print(len(numb))