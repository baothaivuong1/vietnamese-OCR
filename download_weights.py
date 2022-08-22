from tool.utils2 import download_pretrained_weights

download_pretrained_weights("pan_resnet18_sroie19", cached="weights/PANNet_best_map.pth")
download_pretrained_weights("transformerocr_mcocr", cached="weights/transformerocr.pth")
download_pretrained_weights("phobert_mcocr", cached="weights/phobert_report.pth")