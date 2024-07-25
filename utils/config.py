from pathlib import Path
from typing import Final, Self

import yaml
from pydantic import BaseModel

from .const import (
    DIR_CONF,
    DIR_DEFAULT_CONF,
    FNAME_CONF_FORMAT,
    FNAME_CONF_LABELS,
    FNAME_CONF_ROIS,
)

__all__ = [
    "FormatsConfig",
    "LabelsConfig",
    "ROIsConfig",
    "CONF_FORMATS",
    "CONF_LABELS",
    "CONF_ROIS",
]


class YAMLConfig(BaseModel):
    @staticmethod
    def _load_conf_dict(fname: str) -> dict:
        conf_path: Path = DIR_CONF / fname
        default_conf_path: Path = DIR_DEFAULT_CONF / fname
        try:
            with open(default_conf_path, "r") as f:
                conf_dict: dict = yaml.safe_load(f)
        except FileNotFoundError as e:
            print(
                f"{e}.  Please download it and place it in {DIR_DEFAULT_CONF}"
            )
            raise

        try:
            with open(conf_path, "r") as f:
                conf_dict.update(yaml.safe_load(f))
        except FileNotFoundError:
            pass
        return conf_dict

    @classmethod
    def _load(cls, fname: str) -> Self:
        conf_dict = cls._load_conf_dict(fname)
        return cls(**conf_dict)

    @classmethod
    def load(cls) -> Self:
        raise NotImplementedError


class FormatsConfig(YAMLConfig):
    datatype_stimulation_label: str
    process_similarity_field: str

    @classmethod
    def load(cls) -> Self:
        return cls._load(FNAME_CONF_FORMAT)

    def format_label_dtype_stim(self, data_type: str, stimulation: str) -> str:
        return eval(f'f"{self.datatype_stimulation_label}"')

    def format_field_proc_sim(
        self, process_method: str, similarity_method: str
    ) -> str:
        return eval(f'f"{self.process_similarity_field}"')


class _LabelsConfDType(BaseModel):
    shuffled: str
    real: str


class _LabelsConfProcM(BaseModel):
    original: str


class LabelsConfig(YAMLConfig):
    data_type: _LabelsConfDType
    process_method: _LabelsConfProcM

    @classmethod
    def load(cls) -> Self:
        return cls._load(FNAME_CONF_LABELS)


class _ConfRegionInfo(BaseModel):
    name: str
    center: list
    specific_stimulation: str


class ROIsConfig(YAMLConfig):
    shape_ROI: list
    regions: list[_ConfRegionInfo]

    @classmethod
    def load(cls) -> Self:
        return cls._load(FNAME_CONF_ROIS)

    def _get_region_info(self, name: str) -> _ConfRegionInfo:
        for region in self.regions:
            if region.name == name:
                return region
        raise ValueError(f'Region "{name}" not found')

    def _get_axis_slice(self, len_axis: int, center: int) -> slice:
        start = center - len_axis // 2
        return slice(start, start + len_axis)

    def get_roi_slices(self, name: str) -> list[slice]:
        region_info = self._get_region_info(name)
        roi_slices = []
        for len_axis, axis_center in zip(self.shape_ROI, region_info.center):
            roi_slices.append(
                self._get_axis_slice(len_axis=len_axis, center=axis_center)
            )
        return roi_slices

    def get_roi_spec_stim(self, name: str) -> str:
        region_info = self._get_region_info(name)
        return region_info.specific_stimulation


CONF_FORMATS: Final[FormatsConfig] = FormatsConfig.load()
CONF_LABELS: Final[LabelsConfig] = LabelsConfig.load()
CONF_ROIS: Final[ROIsConfig] = ROIsConfig.load()
