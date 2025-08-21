# 🛠️ 2025-08-21 기술 업데이트 요약

## 🔹 Kubernetes - Tuning Linux Swap for Kubernetes: A Deep Dive
이 기술 블로그 글은 Kubernetes v1.34 릴리스에서 도입될 예정인 NodeSwap 기능을 통해 Linux 노드에서 스왑 사용을 허용하는 방법에 대해 설명합니다. 이는 전통적으로 성능 예측 가능성을 위해 스왑을 비활성화하던 관행에서의 중요한 변화입니다. 스왑은 물리적 RAM이 부족할 때 추가 가상 메모리로서 사용할 수 있도록 하며, 자원 활용도를 높이고 메모리 부족(OOM)으로 인한 프로세스 종료를 줄이려는 목적을 가지고 있습니다.

그러나 스왑을 활성화하는 것이 간단한 솔루션은 아닙니다. 메모리 압박 상황에서 노드의 성능과 안정성은 Linux 커널의 몇 가지 주요 매개변수 설정에 크게 의존합니다. 잘못된 설정은 성능 저하를 초래할 수 있으며, Kubelet의 퇴거 논리에 간섭할 수 있습니다.

이 글은 스왑 동작을 제어하는 중요한 Linux 커널 매개변수에 대해 심도 있게 설명하고, 이러한 매개변수가 Kubernetes 워크로드 성능, 스왑 활용, 그리고 중요한 퇴거 메커니즘에 어떻게 영향을 미치는지를 탐구합니다. 또한 다양한 설정의 영향을 보여주는 테스트 결과를 제시하고, 안정적이고 높은 성능을 발휘하는 Kubernetes 클러스터를 위한 최적의 설정을 찾기 위한 연구 결과를 공유합니다.

마지막으로, 스왑 활성화의 위험성과 이를 관리하기 위한 권장 사항을 제시합니다. 스왑을 사용하는 것은 성능 저하, 메모리 누수 감지 어려움, 퇴거 비활성화와 같은 위험을 동반할 수 있습니다. 적절한 매개변수 설정을 통해 이러한 위험을 관리할 수 있습니다. 특히, Kubernetes 환경에서의 적절한 설정을 통해 OOM 킬을 방지하고, 시스템 안정성을 유지하기 위한 시작점을 권장합니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/08/19/tuning-linux-swap-for-kubernetes-a-deep-dive/)

## 🔹 Spring Boot - Spring Batch 6.0.0-M2 available now
Spring Batch 6.0.0-M2 버전이 Maven Central에 출시되었습니다. 이번 마일스톤 릴리스에서는 종속성 업그레이드, 청크 지향 처리 모델의 새로운 구현, 갑작스러운 작업 실행 실패 복구 기능이 추가되었습니다. Spring 종속성은 Spring Framework 7.0.0-M8 등으로 업그레이드되었으며, 청크 지향 처리 모델의 새로운 구현은 이제 안정 버전으로 제공됩니다. 또한, 모든 작업 저장소에서 일관되게 실패한 작업 실행을 복구할 수 있는 새로운 메서드도 도입되었습니다. 더 자세한 내용은 릴리스 노트를 참고하세요.
👉 [자세히 보기](https://spring.io/blog/2025/08/20/spring-batch-6)

## 🔹 Docker - The Supply Chain Paradox: When “Hardened” Images Become a Vendor Lock-in Trap
제목: 공급망 역설: "강화된" 이미지가 공급업체 종속의 함정이 될 때

요약: 보안에 민감한 조직들이 최소한의 운영 부담으로 즉각적인 보안을 추구함에 따라, 사전 강화된 컨테이너 이미지 시장이 급성장하고 있습니다. 최소한의 종속성을 가진 강화된 이미지는 기본적으로 제공되는 보안을 약속하여, 팀이 저수준의 구성 관리를 반복하지 않고 애플리케이션 구축 및 배포에 집중할 수 있게 합니다. 그러나 이는 공급업체 종속의 위험을 수반할 수 있으며, 이에 대한 주의가 필요합니다.
👉 [자세히 보기](https://www.docker.com/blog/hardened-container-images-security-vendor-lock-in/)

## 🔹 Java - Auto-Vectorization in HotSpot #JVMLS
이 기술 블로그 글은 HotSpot C2의 자동 벡터화 기능의 개발 및 개선 사항에 대해 다루고 있습니다. 글에서는 SuperWord 알고리즘에 대한 간단한 소개 후, 이미 이루어진 중요한 향상점과 향후 발전 계획을 실제 사례와 벤치마크를 통해 설명하고 있습니다.
👉 [자세히 보기](https://inside.java/2025/08/16/jvmls-hotspot-auto-vectorization/)

## 🔹 Golang - Container-aware GOMAXPROCS
블로그 글은 Go 1.25 버전에서 도입된 새로운 GOMAXPROCS 기본값이 컨테이너 환경에서의 성능을 개선한다는 내용을 다루고 있습니다. 이 업데이트는 Go 런타임이 컨테이너의 CPU 할당을 자동으로 인식하고 이에 맞춰 GOMAXPROCS 값을 조정함으로써 리소스 사용 효율성을 높입니다.
👉 [자세히 보기](https://go.dev/blog/container-aware-gomaxprocs)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
제목: Helm @ KubeCon + CloudNativeCon EU '25

요약: Helm 팀이 2025년 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU에 참가합니다. 올해 말 출시 예정인 Helm 4에 대한 논의에 참여할 수 있는 기회가 제공되며, 발표 세션과 프로젝트 파빌리온의 Helm 부스에서 유지 관리자들과 직접 대화할 수 있습니다. 주간 동안 진행될 Helm 관련 활동의 세부 사항은 링크를 통해 확인할 수 있습니다.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

