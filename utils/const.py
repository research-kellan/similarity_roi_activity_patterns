from enum import StrEnum
from pathlib import Path
from typing import Final


# Fields
class _FieldsImgDB:
    DTYPE = "data_type"
    STIM = "stimulation"
    SUBJ = "subject"
    IMGS = "images"


class _FieldsSims:
    SIMS = "similarities"


class FieldsSimsDB(StrEnum):
    SUBJ_ID = "subject ID"
    PROC_M = "process method"
    SIM_M = "similarity method"
    SIM = "similarity"


class FieldsWholeBrain(_FieldsImgDB, _FieldsSims, StrEnum):
    pass


class _FieldsSpec:
    SPEC_TYPE = "specificity type"


class FieldsROI(_FieldsImgDB, _FieldsSims, _FieldsSpec, StrEnum):
    REGION = "region"
    AS_STD_PAT = "as standard pattern"


class FieldsAvgSimsDB(StrEnum):
    SUBSET_TYPE = "subset type"


# Configuration file names
FNAME_CONF_FORMAT: Final[str] = "formats.yaml"
FNAME_CONF_LABELS: Final[str] = "labels.yaml"
FNAME_CONF_ROIS: Final[str] = "ROIs.yaml"


# Paths
DIR_PROJECT: Final[Path] = Path(__file__).parents[1]
DIR_DATA: Final[Path] = DIR_PROJECT / "data"
DIR_CONF: Final[Path] = DIR_PROJECT / "config"
DIR_COMP: Final[Path] = DIR_PROJECT / "components"
DIR_DEFAULT_CONF: Final[Path] = DIR_COMP / "default_config"
