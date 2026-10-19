"""Label schema per thread, based on the codebook in '03 - Voice of Customer.xlsx' and the
VOC template in the Launch Blueprint (section 2.3)."""

from __future__ import annotations

from typing import Literal, Optional

from pydantic import BaseModel, Field

Region = Literal[
    "heel", "arch", "forefoot", "toes", "midfoot", "top_of_foot", "ankle", "achilles",
    "whole_foot", "nerve", "skin", "legs_knees_back",
]
Situation = Literal[
    "standing_work", "walking_work", "work_boots", "healthcare_shift", "hospitality", "retail",
    "warehouse_factory", "construction", "office", "teaching", "running", "hiking", "sport",
    "daily_walking", "travel", "pregnancy", "overweight", "aging", "after_injury", "other",
]
SolutionCategory = Literal[
    "otc_insole", "custom_orthotic", "copper_or_magnetic", "acupressure_reflexology", "shoes",
    "barefoot_minimal", "heel_cup_gel_pad", "metatarsal_pad", "stretching_exercise", "physio",
    "massage_rolling", "night_splint", "compression_socks", "taping", "rest_ice", "weight_loss",
    "medication_injection", "shockwave", "surgery", "doctor_podiatrist", "lifestyle_other", "other",
]
Verdict = Literal["works", "partly", "no_effect", "made_worse", "mixed", "unknown"]
Complaint = Literal[
    "too_thick", "too_hard", "too_soft", "flattened_wore_out", "arch_too_high", "arch_too_low",
    "bad_pad_position", "heel_too_high", "toe_box_tight", "slipping", "heat_sweat", "odor",
    "squeaky", "sizing_trimming", "too_expensive", "no_effect", "made_worse", "short_lived_effect",
    "other",
]
QuoteKind = Literal["pain", "impact_on_life", "desire", "objection", "works", "fails", "copper", "buying_trigger"]


class Quote(BaseModel):
    text: str = Field(description="Exact, verbatim fragment uit de bron (max ~2 zinnen). Nooit herschrijven.")
    source_id: str = Field(description="'post' of de comment-id waar het citaat uit komt")
    kind: QuoteKind
    nl_meaning: str = Field(description="Getrouwe Nederlandse betekenis (T), geen marketingtekst")


class Solution(BaseModel):
    solution: str = Field(description="Wat iemand probeerde of aanraadt, kort en concreet")
    category: SolutionCategory
    brand_or_product: Optional[str] = Field(description="Merk/product indien genoemd, anders null")
    verdict: Verdict
    first_hand: bool = Field(description="True als de schrijver het zelf gebruikt heeft")
    reason: str = Field(description="Waarom het (niet) werkte, in het Nederlands")
    source_id: str = Field(description="'post' of de comment-id")


class CopperView(BaseModel):
    mentioned: bool
    sentiment: Literal["positive", "negative", "skeptical", "neutral", "mixed", "not_mentioned"]
    summary_nl: str = Field(description="Wat er over koper/magneten/wellness-zolen gezegd wordt; leeg als niet genoemd")


class ThreadLabel(BaseModel):
    relevant: bool = Field(description="Gaat de thread echt over voeten, voetklachten, schoeisel- of zoolcomfort?")
    language: Literal["en", "nl", "de", "other"]
    thread_type: Literal[
        "asking_help", "experience_report", "recommendation_request", "product_review", "rant",
        "discussion", "other",
    ]
    problem_summary_nl: str = Field(description="Het kernprobleem van de vraagsteller in 1-2 zinnen, Nederlands")
    regions: list[Region]
    conditions: list[str] = Field(description="Genoemde aandoeningen in het Engels, zoals 'plantar fasciitis'")
    diagnosed_by_professional: Optional[bool] = Field(description="null als onbekend")
    occupation: Optional[str] = Field(description="Beroep van de vraagsteller indien genoemd")
    situations: list[Situation]
    duration: Optional[str] = Field(description="Hoe lang de klacht al speelt, indien genoemd")
    previous_fixes: list[str] = Field(description="Wat de vraagsteller al geprobeerd had")
    complaints_about_products: list[Complaint]
    desired_outcomes_nl: list[str] = Field(description="Wat mensen eigenlijk willen (weer kunnen wandelen, dienst volhouden...)")
    solutions: list[Solution] = Field(description="Alle oplossingen uit post en reacties, één per (oplossing, schrijver)")
    brands_mentioned: list[str]
    copper: CopperView
    price_mentions: list[str] = Field(description="Bedragen of prijsbezwaren, letterlijk")
    quotes: list[Quote] = Field(description="3-10 sterkste letterlijke citaten")
    emotional_intensity: Literal[1, 2, 3, 4, 5]
    medical_red_flag: bool = Field(description="Diabetes, neuropathie, gevoelloosheid, infectie, breuk, ernstige zwelling")
    claims_risk: Literal["comfort_only", "material", "medical"]
    marketing_insight_nl: str = Field(description="Eén inzicht voor positionering/advertentie (A/H), duidelijk als hypothese")
