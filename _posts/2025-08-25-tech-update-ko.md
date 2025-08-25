# 🛠️ 2025-08-25 기술 업데이트 요약

## 🔹 Kubernetes - Tuning Linux Swap for Kubernetes: A Deep Dive
이 기술 블로그 글은 Kubernetes v1.34 릴리스에서 안정화될 예정인 NodeSwap 기능을 중심으로, Linux 노드에서 스왑을 조정하는 방법에 대해 다룹니다. 이 기능은 물리적 RAM이 부족할 때 추가 가상 메모리를 제공하기 위해 스왑을 사용할 수 있게 하여 리소스 활용을 개선하고 OOM(Out-of-Memory) 킬을 줄이는 것을 목표로 합니다. 그러나 스왑을 활성화하는 것은 단순히 설정을 켜는 것만으로 해결되지 않으며, 올바른 Linux 커널 매개변수 조정이 중요합니다. 잘못된 설정은 성능 저하와 Kubelet의 퇴출 로직에 영향을 줄 수 있습니다.

글은 Linux의 스왑 동작을 제어하는 주요 커널 매개변수인 `vm.swappiness`, `vm.min_free_kbytes`, `vm.watermark_scale_factor`를 설명하며, 각각이 Kubernetes 워크로드 성능, 스왑 사용 및 퇴출 메커니즘에 미치는 영향을 다룹니다. 또한 다양한 테스트 결과를 통해 최적의 설정을 찾아내는 과정을 공유합니다.

스왑 사용과 관련된 위험으로는 성능 저하, 메모리 누수 은폐, 퇴출 메커니즘 비활성화 등이 있으며, 이를 관리하기 위해 신중한 조정이 필요하다고 강조합니다. 마지막으로, 스왑을 처음 설정할 때 자신의 워크로드에 맞춰 벤치마크 테스트를 권장합니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/08/19/tuning-linux-swap-for-kubernetes-a-deep-dive/)

## 🔹 Spring Boot - Spring Modulith 2.0 M2, 1.4.3, and 1.3.9 released
Spring Modulith 2.0 M2, 1.4.3, 1.3.9 버전이 출시되었습니다. 이번 릴리스에서는 버그 수정과 일반적인 종속성 업그레이드 외에도 몇 가지 새로운 기능이 추가되었습니다. 2.0 M2 버전의 주요 기능으로는 MongoDB와 Neo4j의 이벤트 발행 저장소 구현 업데이트, `ApplicationModulesEndpoint`의 부트스트랩 절차 개선, Spring Boot 4.0 M2로의 업그레이드가 포함되어 있습니다. 더 자세한 내용은 각 버전의 변경 로그에서 확인할 수 있습니다.
👉 [자세히 보기](https://spring.io/blog/2025/08/22/spring-modulith-2-0-0-m2-1-4-3-and-1-3-9-released)

## 🔹 Docker - Prototyping an AI Tutor with Docker Model Runner
이 기술 블로그 글은 Docker의 Model Runner를 사용하여 AI 튜터를 프로토타이핑하는 방법에 대해 설명합니다. 글의 시작에서는 많은 개발자들이 처음으로 `docker run hello-world` 명령어를 실행할 때 느낀 흥분과 경이로움을 언급합니다. 이러한 경험을 AI가 어떻게 더 개선할 수 있을지를 탐구합니다. 글의 저자는 Docker의 문서 팀에서 일하며, 개발자 경험을 향상시키기 위한 방법을 고민한다고 설명합니다. 이 글은 AI를 활용하여 Docker 사용 경험을 어떻게 향상시킬 수 있을지를 다룹니다.
👉 [자세히 보기](https://www.docker.com/blog/how-to-build-an-ai-tutor-with-model-runner/)

## 🔹 Java - How to Upgrade to Java 25 #RoadTo25
기술 블로그 글 "How to Upgrade to Java 25 #RoadTo25"는 Java 21에서 25로의 업그레이드가 일반적으로 원활하게 이루어진다고 설명합니다. 하지만 프로젝트에 따라서는 주석 처리, 널 체크, 파일 작업 또는 오래된 기술의 제거와 같은 세부 사항이 문제를 일으킬 수 있습니다. 이러한 모든 세부 사항을 Peter가 수집하여 설명합니다.
👉 [자세히 보기](https://inside.java/2025/08/24/roadto25-upgrade/)

## 🔹 Golang - Container-aware GOMAXPROCS
제목: 컨테이너 인식 GOMAXPROCS

요약: Go 1.25 버전에서 새로운 GOMAXPROCS 기본값이 도입되어 컨테이너 환경에서의 성능이 개선되었습니다. 이 업데이트는 Go 프로그래밍 언어가 컨테이너에서 더 효율적으로 작동할 수 있도록 지원합니다.
👉 [자세히 보기](https://go.dev/blog/container-aware-gomaxprocs)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
블로그 글 요약: Helm 팀이 2025년 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU '25에 참석합니다. 올해 말 출시 예정인 Helm 4에 대한 논의에 참여하고 싶다면, 발표 세션과 Project Pavilion의 Helm 부스를 방문해 보세요. 주간 동안 진행되는 Helm 관련 활동에 대한 자세한 내용은 블로그에서 확인할 수 있습니다.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

