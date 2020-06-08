from typing import Dict, TypedDict, TypeVar

from kubernetes_asyncio.client.models import (
    V1beta1CronJob,
    V1ConfigMap,
    V1Deployment,
    V1PersistentVolume,
    V1PersistentVolumeClaim,
    V1Secret,
    V1Service,
    V1StatefulSet,
)

LabelType = Dict[str, str]
K8sModel = TypeVar(
    "K8sModel",
    V1beta1CronJob,
    V1ConfigMap,
    V1Deployment,
    V1PersistentVolume,
    V1PersistentVolumeClaim,
    V1Secret,
    V1Service,
    V1StatefulSet,
)


class SecretKeyRef(TypedDict):
    key: str
    name: str


class SecretKeyRefContainer(TypedDict):
    secretKeyRef: SecretKeyRef
