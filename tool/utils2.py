import gdown

def download_weights(id_or_url, cached=None, md5=None, quiet=False):
    if id_or_url.startswith('http'):
        url = id_or_url
    else:
        url = 'https://drive.google.com/uc?id={}'.format(id_or_url)

    return gdown.cached_download(url=url, path=cached, md5=md5, quiet=quiet)


weight_url = {
    "pan_resnet18_default": "1GKs-NnezTc6WN0P_Zw7h6wYzRRZdJFKl" ,
    "pan_resnet18_sroie19": "1-QvIN0MrP28URQILYvLaF1G1eTx2oh8W" ,
    "transformerocr_mcocr": "1qpXp_-digz2HPTGY_GPdwstzGLhjC_ot",
    "transformerocr_default_vgg": "13327Y1tz1ohsm5YZMyXVMPIOjoOA0OaA",
    "transformerocr_default_resnet50": "12dTOZ9VP7ZVzwQgVvqBWz5JO5RXXW5NY",
    "transformerocr_default_resnet50_fpn": "12dTOZ9VP7ZVzwQgVvqBWz5JO5RXXW5NY",
    "transformerocr_config": "1xQqR9swWNCTLEa0ensPDT0HDBHTke3xT",
    "phobert_mcocr": "1v4GQPg4Jx5FWvqJ-2k9YCxEd6iFdlXXa"
}


def download_pretrained_weights(name, cached=None):
    return download_weights(weight_url[name], cached)