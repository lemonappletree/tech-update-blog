# 🛠️ 2025-08-26 기술 업데이트 요약

## 🔹 Kubernetes - Tuning Linux Swap for Kubernetes: A Deep Dive
이 기술 블로그 글은 Kubernetes v1.34 버전의 새로운 기능인 NodeSwap을 소개하고, 리눅스 시스템에서 스왑 메모리를 효과적으로 조율하는 방법을 설명합니다. 스왑 메모리를 활성화하면 물리적 RAM이 부족할 때 추가적인 가상 메모리를 사용하여 리소스 활용을 개선하고 OOM(Out-Of-Memory) 종료를 줄일 수 있습니다. 그러나 스왑을 활성화하는 것만으로는 충분하지 않으며, 성능과 안정성은 리눅스 커널 매개변수 설정에 크게 의존합니다.

글은 리눅스 커널의 스왑 동작을 제어하는 주요 매개변수, 특히 `vm.swappiness`, `vm.min_free_kbytes`, `vm.watermark_scale_factor`를 상세히 다룹니다. 이러한 매개변수들이 Kubernetes 워크로드 성능, 스왑 활용, 그리고 중요한 퇴출 메커니즘에 어떻게 영향을 미치는지를 설명하고, 다양한 설정에 따른 테스트 결과를 공유하며 안정적이고 높은 성능의 Kubernetes 클러스터를 위한 최적의 설정을 제안합니다.

또한, 스왑 사용의 위험성과 그에 따른 권장 설정을 설명하며, Kubernetes 환경에서 스왑을 활용할 때 고려해야 할 사항들을 다룹니다. 블로그 글은 각각의 워크로드에 맞춰 스왑 설정을 조정할 것을 권장하며, 테스트 환경에서 벤치마크 테스트를 수행하여 최적의 성능을 얻을 수 있도록 합니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/08/19/tuning-linux-swap-for-kubernetes-a-deep-dive/)

## 🔹 Spring Boot - Spring Modulith 2.0 M2, 1.4.3, and 1.3.9 released
Spring Modulith 2.0 M2, 1.4.3 및 1.3.9 버전이 출시되었습니다. 버그 수정 릴리스에는 일반적인 종속성 업그레이드와 몇 가지 사소한 개선 사항이 포함되어 있습니다. 2.0 M2 버전에는 다음과 같은 새로운 기능이 추가되었습니다: MongoDB 및 Neo4j를 위한 이벤트 발행 저장소 구현 업데이트, `ApplicationModulesEndpoint`의 부트스트랩 절차 개선, Spring Boot 4.0 M2로 업그레이드. 자세한 내용은 각 버전의 전체 변경 로그를 참조하세요.
👉 [자세히 보기](https://spring.io/blog/2025/08/22/spring-modulith-2-0-0-m2-1-4-3-and-1-3-9-released)

## 🔹 Docker - Prototyping an AI Tutor with Docker Model Runner
이 기술 블로그 글은 Docker Model Runner를 사용하여 AI 튜터를 프로토타입하는 방법에 대해 설명합니다. 글의 저자는 개발자 경험을 향상시키기 위해 AI를 활용할 수 있는 방법을 탐구하며, 특히 Docker 초보자들에게 친숙한 'docker run hello-world' 명령어의 경험을 AI가 어떻게 개선할 수 있는지에 대해 논의합니다. 이 글에서는 AI 기술을 활용하여 개발자들이 Docker를 더 쉽게 이해하고 활용할 수 있도록 돕는 방법을 제안합니다.
👉 [자세히 보기](https://www.docker.com/blog/how-to-build-an-ai-tutor-with-model-runner/)

## 🔹 Java - How to Upgrade to Java 25 #RoadTo25
제목: Java 25로 업그레이드하는 방법 #RoadTo25

요약: Java 21에서 Java 25로의 업그레이드는 일반적으로 원활하게 진행됩니다. 그러나 주석 처리, null 체크, 파일 작업, 오래된 기술의 제거 등 작은 변화들이 모여 있는 프로젝트라면 다소 어려움을 겪을 수 있습니다. Peter는 이러한 모든 세부 사항을 수집하여 정리하고 있습니다.
👉 [자세히 보기](https://inside.java/2025/08/24/roadto25-upgrade/)

## 🔹 Golang - Container-aware GOMAXPROCS
블로그 글 요약: Go 1.25 버전에서는 GOMAXPROCS의 기본 설정이 개선되어, 컨테이너 환경에서의 성능과 동작이 향상되었습니다. 이러한 업데이트는 컨테이너 내에서 애플리케이션이 시스템의 가용 리소스를 보다 효과적으로 활용할 수 있도록 돕습니다.
👉 [자세히 보기](https://go.dev/blog/container-aware-gomaxprocs)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
제목: Helm @ KubeCon + CloudNativeCon EU '25

Helm 팀이 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU '25에 참가합니다. 올해 말에 출시될 예정인 Helm 4에 대한 논의가 진행될 예정이니, 발표 세션과 프로젝트 파빌리온 내의 Helm 부스에서 유지 관리자들과 대화를 나눠보세요. 주간 동안 진행될 모든 Helm 관련 활동에 대한 자세한 내용은 링크에서 확인할 수 있습니다.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

