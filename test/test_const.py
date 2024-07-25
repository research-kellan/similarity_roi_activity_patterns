import sys
from pathlib import Path

_ROOT_PROJECT = Path(__file__).parents[1]
sys.path.insert(0, _ROOT_PROJECT.as_posix())
from utils.const import (
    DIR_COMP,
    DIR_CONF,
    DIR_DATA,
    DIR_DEFAULT_CONF,
    DIR_PROJECT,
    FNAME_CONF_FORMAT,
    FNAME_CONF_LABELS,
    FNAME_CONF_ROIS,
    FieldsAvgSimsDB,
    FieldsROI,
    FieldsSimsDB,
    FieldsWholeBrain,
)

consts = [
    FieldsAvgSimsDB,
    FieldsROI,
    FieldsSimsDB,
    FieldsWholeBrain,
    FNAME_CONF_FORMAT,
    FNAME_CONF_LABELS,
    FNAME_CONF_ROIS,
    DIR_COMP,
    DIR_CONF,
    DIR_DATA,
    DIR_DEFAULT_CONF,
    DIR_PROJECT,
]

for const in consts:
    print(const, end="\n\n")
