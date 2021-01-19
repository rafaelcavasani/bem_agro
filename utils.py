from osgeo import gdal, osr


def get_image_info(path):
    ds = gdal.Open(r'images/talhao_ponkan.tif')
    prj = ds.GetProjection()
    # print(prj)

    srs = osr.SpatialReference(wkt=prj)
    if srs.IsProjected:
        print(srs.GetAttrValue('projcs'))
    print(srs.GetAttrValue('geogcs')) 