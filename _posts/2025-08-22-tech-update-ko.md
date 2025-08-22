# 🛠️ 2025-08-22 기술 업데이트 요약

## 🔹 Kubernetes - Tuning Linux Swap for Kubernetes: A Deep Dive
이 기술 블로그 글은 Kubernetes v1.34 릴리스에서 NodeSwap 기능이 안정화되면서 리눅스 노드에서 스왑을 사용하는 방법에 대해 설명합니다. 스왑은 물리적 RAM이 부족할 때 가상 메모리를 추가로 사용할 수 있도록 하여 자원 활용을 개선하고 OOM 킬을 줄이는 데 목적이 있습니다. 그러나 스왑 기능을 활성화하는 것은 간단한 작업이 아니며, 리눅스 커널의 다양한 매개변수 설정에 따라 노드의 성능과 안정성이 크게 영향을 받을 수 있습니다. 글에서는 스왑 동작을 제어하는 주요 커널 매개변수를 다루고, Kubernetes 작업 부하 성능과 스왑 사용률, 그리고 중요한 퇴거 메커니즘에 미치는 영향을 설명합니다. 스왑 조정을 위한 테스트 결과와 최적 설정을 통해 안정적이고 고성능의 Kubernetes 클러스터를 구축하는 방법을 공유합니다. 중요한 커널 매개변수로는 `vm.swappiness`, `vm.min_free_kbytes`, `vm.watermark_scale_factor` 등이 있으며, 각 매개변수가 노드 성능에 미치는 영향을 실험을 통해 분석하고 최적의 설정을 제안합니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/08/19/tuning-linux-swap-for-kubernetes-a-deep-dive/)

## 🔹 Spring Boot - A Bootiful Podcast: Andrey Belyaev, product manager for IntelliJ IDEA
이 블로그 글은 "A Bootiful Podcast" 시리즈의 일환으로, JetBrains에서 IntelliJ IDEA 제품 매니저로 일하고 있는 Andrey Belyaev와의 인터뷰를 다루고 있습니다. 이 인터뷰에서는 JetBrains의 IntelliJ IDEA가 Spring을 지원하는 최신 기능에 대해 논의합니다.
👉 [자세히 보기](https://spring.io/blog/2025/08/21/a-bootiful-podcast-andrey-belyaev)

## 🔹 Docker - Prototyping an AI Tutor with Docker Model Runner
블로그 글은 Docker의 Model Runner를 사용하여 AI 튜터를 프로토타이핑하는 방법에 대해 설명합니다. 글쓴이는 개발자들이 처음으로 `docker run hello-world` 명령어를 실행할 때 느꼈던 흥분과 호기심을 AI를 통해 더욱 향상시킬 수 있는 방법을 탐구합니다. Docker의 기술 문서 팀에서 일하는 작가는 개발자 경험을 개선하는 데 중점을 두고 있으며, AI 튜터를 통해 사용자들이 Docker를 보다 쉽게 이해하고 활용할 수 있도록 돕고자 합니다.
👉 [자세히 보기](https://www.docker.com/blog/how-to-build-an-ai-tutor-with-model-runner/)

## 🔹 Java - Growing the Java Language #JVMLS
이 기술 블로그 글은 2025 JVM Language Summit에서 Java 언어 아키텍트인 Brian Goetz가 Java 언어 발전에 대해 발표한 내용을 다룹니다. Goetz는 Java 언어의 진화를 위해 새로운 기능 및 개선 사항을 어떻게 도입할 계획인지 설명하며, Java의 미래 방향성을 제시합니다. 이 글은 Java 개발자들이 앞으로 주목해야 할 변화와 업데이트에 대한 통찰을 제공합니다.
👉 [자세히 보기](https://inside.java/2025/08/21/jvmls-growing-java-language/)

## 🔹 Golang - Container-aware GOMAXPROCS
제목: 컨테이너 인식 GOMAXPROCS

요약: Go 1.25 버전에서 새롭게 적용된 GOMAXPROCS 기본값은 컨테이너 환경에서의 성능을 개선합니다.
👉 [자세히 보기](https://go.dev/blog/container-aware-gomaxprocs)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
블로그 글 요약: Helm 팀이 2025년 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU에 참가합니다. 올해 말 출시 예정인 Helm 4에 대한 논의에 참여할 수 있는 기회가 마련되어 있으며, 발표 세션 및 프로젝트 파빌리온 내 Helm 부스에서 유지관리자들과 대화할 수 있습니다. 행사 기간 동안 Helm과 관련된 다양한 활동에 대한 자세한 정보는 블로그를 참조하세요.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

