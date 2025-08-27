# 🛠️ 2025-08-27 기술 업데이트 요약

## 🔹 Kubernetes - Tuning Linux Swap for Kubernetes: A Deep Dive
이 블로그 글은 Kubernetes v1.34 릴리스에서 안정화될 예정인 NodeSwap 기능을 통해 Linux 노드에서 스왑 사용을 조정하는 방법을 다룹니다. 스왑을 활성화하면 물리적 RAM이 부족할 때 추가 가상 메모리를 사용할 수 있어 리소스 활용도를 높이고 메모리 부족(OOM) 문제를 줄일 수 있습니다. 그러나 스왑을 활성화하는 것은 단순한 해결책이 아니며, Linux 커널의 여러 매개변수 조정에 따라 노드의 성능과 안정성이 크게 달라질 수 있습니다.

글에서는 스왑 동작을 관리하는 중요한 Linux 커널 매개변수들을 소개하고, 이들이 Kubernetes 워크로드 성능, 스왑 사용량, 그리고 퇴출 메커니즘에 미치는 영향을 설명합니다. 다양한 설정의 테스트 결과를 통해 최적의 설정을 찾는 과정을 공유합니다.

스왑 조정에 있어 주목할 커널 매개변수로는 `vm.swappiness`, `vm.min_free_kbytes`, `vm.watermark_scale_factor` 등이 있습니다. 각 매개변수는 스왑과 메모리 사용에 중요한 역할을 하며, 올바른 설정을 통해 시스템의 OOM 킬을 방지하고 안정성을 유지할 수 있습니다. 블로그 글은 이러한 매개변수를 적절히 조정하여 Kubernetes 클러스터에서 스왑을 효과적으로 사용하는 방법을 제안합니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/08/19/tuning-linux-swap-for-kubernetes-a-deep-dive/)

## 🔹 Spring Boot - This Week in Spring - August 26th, 2025
이번 주 Spring 블로그 요약:

- SpringOne 행사에서 작성된 이번 글에서는 다양한 소식이 전해졌습니다.
- 저번 주 "A Bootiful Podcast"에서는 IntelliJ IDEA의 제품 관리자 Andrey Belyaev와의 인터뷰가 있었습니다.
- Spring Boot 4.0.0.M2, Spring Batch 6.0.0.M2, Spring Authorization Server 2.0.0 M2 등이 출시되었습니다.
- Spring Modulith 2.0 M2와 관련 버전들도 릴리스되었습니다.
- Spring Boot 4와 Spring Framework 7의 새로운 기능에 대한 Loiane Groner의 설명이 있습니다.
- Docker를 활용한 Spring AI 빌드 단순화에 관한 유용한 정보가 제공됩니다.
- Flyway와 Spring Boot를 사용하는 튜토리얼도 소개됩니다.
- Spring Office Hours에 참여한 경험을 공유했습니다.
- CQRS와 Spring Modulith에 대한 간단한 해설이 있습니다.
- Embabel과 Spring 창립자 Rod Johnson의 새로운 Spring AI 프레임워크에 대한 비교 시리즈가 소개됩니다.
- AWS에서 Spring AI를 활용한 Java AI 에이전트 구축 워크숍이 있었습니다.
- "JSpecify: Java Nullness Annotations and Kotlin"이라는 주제로 David Baker의 강연이 있었습니다.
👉 [자세히 보기](https://spring.io/blog/2025/08/26/this-week-in-spring-august-26th-2025)

## 🔹 Docker - Prototyping an AI Tutor with Docker Model Runner
이 기술 블로그 글은 Docker Model Runner를 사용하여 AI 튜터를 프로토타이핑하는 방법에 대해 설명합니다. 글에서는 개발자들이 처음으로 'docker run hello-world' 명령어를 실행했을 때 느끼는 흥미와 경이로움을 AI가 어떻게 더욱 향상시킬 수 있는지에 대해 다룹니다. Docker의 문서팀에서 기술 작가로 일하는 저자는 개발자 경험을 개선하는 데 AI가 어떻게 기여할 수 있는지를 탐구하고 있습니다.
👉 [자세히 보기](https://www.docker.com/blog/how-to-build-an-ai-tutor-with-model-runner/)

## 🔹 Java - How to Upgrade to Java 25 #RoadTo25
기술 블로그 글 요약:

Java 21에서 Java 25로 업그레이드하는 과정은 대체로 원활합니다. 하지만 주석 처리, null 검사, 파일 작업, 오래된 기술의 제거 등 작은 변경 사항들을 모두 포함하고 있는 프로젝트라면 다소 어려울 수 있습니다. 이 글에서는 Peter가 이러한 세부 사항들을 모두 정리하고 있습니다.
👉 [자세히 보기](https://inside.java/2025/08/24/roadto25-upgrade/)

## 🔹 Golang - Container-aware GOMAXPROCS
제목: 컨테이너 인식 GOMAXPROCS  
요약: Go 1.25 버전에서는 컨테이너 환경에서의 성능을 개선하기 위해 새로운 GOMAXPROCS 기본값을 도입했습니다.  
링크: https://go.dev/blog/container-aware-gomaxprocs
👉 [자세히 보기](https://go.dev/blog/container-aware-gomaxprocs)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
블로그 글 요약: Helm 팀이 2025년 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU '25에 참석합니다. Helm 4가 올해 말 출시될 예정이므로, 팀의 유지 보수자들과 대화에 참여하고 발표 세션과 프로젝트 파빌리온의 Helm 부스에서 다양한 활동에 참여할 수 있습니다. 주간 동안의 모든 Helm 관련 활동에 대한 자세한 정보는 블로그에서 확인할 수 있습니다.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

