# 🛠️ 2025-08-24 기술 업데이트 요약

## 🔹 Kubernetes - Tuning Linux Swap for Kubernetes: A Deep Dive
이 블로그 글은 Kubernetes의 NodeSwap 기능을 통한 Linux 스왑 조정에 대해 다루고 있습니다. 이 기능은 Kubernetes v1.34 릴리스에서 안정화될 가능성이 있으며, 이제까지 성능 예측 가능성 때문에 스왑을 비활성화했던 관행에서 벗어나는 중요한 변화입니다. 이 글은 Linux 노드에서 스왑을 조정하는 방법에 초점을 맞추고 있으며, 스왑을 활성화하면 리소스 활용도를 향상시키고 메모리 부족으로 인한 OOM 킬을 줄일 수 있음을 설명합니다. 그러나 스왑을 활성화하는 것이 간단한 해결책은 아니며, Linux 커널 매개변수의 설정에 따라 노드의 성능과 안정성이 크게 좌우될 수 있습니다. 잘못된 설정은 성능 저하와 Kubelet의 퇴출 로직에 방해를 줄 수 있습니다.

블로그 글은 스왑 행동을 결정하는 중요한 Linux 커널 매개변수와 그들이 Kubernetes 작업 부하의 성능, 스왑 활용, 주요 퇴출 메커니즘에 미치는 영향을 탐구합니다. 다양한 설정의 영향을 보여주는 테스트 결과를 제시하고, 안정적이고 성능이 높은 Kubernetes 클러스터를 위한 최적의 설정을 찾는 방법을 공유합니다. 주요 내용은 스왑 조정을 위한 커널 매개변수, 스왑 테스트 및 결과, 리스크와 추천 사항, Kubernetes 문맥에서의 스왑 활용 등을 포함합니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/08/19/tuning-linux-swap-for-kubernetes-a-deep-dive/)

## 🔹 Spring Boot - Spring Modulith 2.0 M2, 1.4.3, and 1.3.9 released
Spring Modulith 2.0 M2, 1.4.3, 및 1.3.9 버전이 출시되었습니다. 이 버그 수정 릴리스는 일반적인 종속성 업그레이드와 몇 가지 작은 개선 사항을 포함하고 있습니다. 2.0 M2 릴리스의 주요 새로운 기능은 다음과 같습니다: MongoDB 및 Neo4j를 위한 이벤트 게시 저장소 구현 업데이트, `ApplicationModulesEndpoint`의 부트스트랩 절차 개선, Spring Boot 4.0 M2로 업그레이드 등이 있습니다. 릴리스에 대한 더 자세한 사항은 전체 변경 로그에서 확인할 수 있습니다.
👉 [자세히 보기](https://spring.io/blog/2025/08/22/spring-modulith-2-0-0-m2-1-4-3-and-1-3-9-released)

## 🔹 Docker - Prototyping an AI Tutor with Docker Model Runner
이 기술 블로그 글은 Docker의 Model Runner를 사용하여 AI 튜터를 프로토타입하는 방법에 대해 설명합니다. 개발자들이 처음으로 `docker run hello-world` 명령어를 실행할 때의 흥분과 경이로움을 AI가 더욱 향상시킬 수 있는 방법을 탐구합니다. 글의 저자인 Docker Docs 팀의 기술 작가는 개발자 경험을 개선하는 방법에 대해 고민하며, 이 글에서는 AI를 통해 사용자가 Docker를 보다 쉽게 이해하고 활용할 수 있도록 돕는 AI 튜터의 프로토타입을 만드는 과정을 소개합니다.
👉 [자세히 보기](https://www.docker.com/blog/how-to-build-an-ai-tutor-with-model-runner/)

## 🔹 Java - Growing the Java Language #JVMLS
블로그 글 제목 "Growing the Java Language #JVMLS"는 2025년 JVM Language Summit에서 Java 언어 아키텍트인 Brian Goetz가 Java 언어의 발전에 대해 발표한 내용을 다루고 있습니다. 이 세션은 Java 언어를 어떻게 발전시킬 것인지에 대한 비전과 계획을 공유하고 있으며, Java의 미래 방향성에 대해 논의하고 있습니다.
👉 [자세히 보기](https://inside.java/2025/08/21/jvmls-growing-java-language/)

## 🔹 Golang - Container-aware GOMAXPROCS
제목: 컨테이너 인식 GOMAXPROCS

요약: Go 1.25 버전에서 GOMAXPROCS의 새로운 기본 설정이 도입되어 컨테이너 환경에서의 성능이 개선되었습니다.
👉 [자세히 보기](https://go.dev/blog/container-aware-gomaxprocs)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
블로그 글 요약: Helm 팀이 2025년 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU에 참가합니다. 올해 말 출시 예정인 Helm 4에 대한 논의가 진행될 예정이니, 발표 세션과 Project Pavilion에 있는 Helm 부스를 찾아가 대화에 참여해 보세요. 주간 동안 진행되는 모든 Helm 관련 활동에 대한 자세한 내용은 블로그에서 확인할 수 있습니다.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

