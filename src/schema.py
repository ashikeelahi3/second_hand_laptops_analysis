from pprint import pprint
from pydantic import BaseModel, Field
from typing import List, Optional


class LaptopSpecs(BaseModel):
    model: str = Field(
        ...,
        description="Full model or series name of the laptop (e.g., 'Dell Inspiron 15 3520', 'HP Pavilion x360')."
    )
    battery_backup: Optional[float] = Field(
        None,
        description="Battery backup duration in hours. If not mentioned, provide a reasonable estimate based on the model and age."
    )
    processor_name: str = Field(
        ...,
        description="Exact processor name (e.g., 'Intel Core i5-1135G7', 'AMD Ryzen 5 4600H'), corrected if the seller misspecified it."
    )
    processor_generation: Optional[str] = Field(
        None,
        description="Processor generation (e.g., '11th Gen', 'Ryzen 4000 series'), derived from the processor name."
    )
    processor_wattage: Optional[float] = Field(
        None,
        description="Approximate TDP (Thermal Design Power) of the processor in watts, inferred from known specifications."
    )
    ram_size: float = Field(
        ...,
        description="Total amount of RAM in gigabytes (GB)."
    )
    ram_generation: Optional[str] = Field(
        None,
        description="RAM generation/type (e.g., 'DDR3', 'DDR4', 'DDR5'). Guess based on model and processor if not given."
    )
    gpu: Optional[str] = Field(
        None,
        description="Graphics processor (e.g., 'NVIDIA GTX 1650', 'Intel Iris Xe', 'AMD Radeon Vega 8'). Guess if not listed."
    )
    gpu_vram: Optional[float] = Field(
        None,
        description="VRAM in gigabytes (GB). For integrated GPUs, give the maximum possible shared memory; for dedicated GPUs, the actual VRAM."
    )
    ssd_size: float = Field(
        0,
        description="SSD storage size in gigabytes (GB). Set to 0 if the laptop has no SSD."
    )
    hdd_size: float = Field(
        0,
        description="HDD storage size in gigabytes (GB). Set to 0 if the laptop has no HDD."
    )
    display_size: float = Field(
        ...,
        description="Display diagonal size in inches (e.g., 15.6)."
    )
    display_resolution: Optional[str] = Field(
        None,
        description="Display resolution in the format 'width x height' (e.g., '1920x1080', '1366x768')."
    )
    time_used_in_moths: int = Field(
        ...,
        description="Time the laptop was used by the seller in months, like 6, 12, etc"
    )


class LaptopList(BaseModel):
    laptops: List[LaptopSpecs] = Field(
        ...,
        description="List of used laptop specifications extracted or inferred from input text."
    )

if __name__ == '__main__':
    from icecream import ic
    for name, field in LaptopSpecs.model_fields.items():
        pprint(f"{name}: {field.annotation} - {field.description}")
