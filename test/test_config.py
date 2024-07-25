import sys
from pathlib import Path

_ROOT_PROJECT = Path(__file__).parents[1]
sys.path.insert(0, _ROOT_PROJECT.as_posix())
from utils.config import CONF_FORMATS, CONF_LABELS, CONF_ROIS

# test ROIsConfig
print(CONF_ROIS)
print(CONF_ROIS.get_roi_slices("STG L"))
print(CONF_ROIS.get_roi_spec_stim("STG L"))


# test FormatsConfig
print(CONF_FORMATS)
print(
    CONF_FORMATS.format_field_proc_sim(
        process_method="hello", similarity_method="world"
    )
)
print(
    CONF_FORMATS.format_label_dtype_stim(
        data_type="hello", stimulation="world"
    )
)


# test LabelsConfig
print(CONF_LABELS)
