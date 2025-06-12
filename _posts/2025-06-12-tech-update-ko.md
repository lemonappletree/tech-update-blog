# 🛠️ 2025-06-12 기술 업데이트 요약

## 🔹 Kubernetes - Enhancing Kubernetes Event Management with Custom Aggregation
이 블로그 글은 Kubernetes 클러스터에서 발생하는 이벤트를 관리하고 분석하는 데 있어서 발생하는 문제점과 이를 해결하기 위한 커스텀 이벤트 집계 시스템 구축 방법에 대해 설명합니다. Kubernetes 이벤트는 클러스터 운영에 대한 중요한 정보를 제공하지만, 클러스터가 커지면서 이벤트의 양, 보존 기간, 관련 이벤트의 상관관계 파악 등의 문제가 발생할 수 있습니다. 이를 해결하기 위해 커스텀 이벤트 집계 시스템을 구축하여 이벤트를 모니터링하고 처리 및 저장하는 방법을 제안합니다. 이 시스템은 이벤트 감시, 처리, 저장을 통해 클러스터 동작을 이해하고 문제를 효과적으로 해결할 수 있게 도와줍니다. 또한, 패턴 감지와 실시간 경고 시스템을 통해 반복적인 문제를 조기에 발견할 수 있는 기능도 제공합니다. 이러한 시스템을 도입함으로써 클러스터 관찰 능력과 문제 해결 능력을 크게 향상시킬 수 있습니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/06/10/enhancing-kubernetes-event-management-custom-aggregation/)

## 🔹 Spring Boot - Spring Tools 4.31.0 released
Spring Tools 4.31.0이 출시되었습니다. 이번 버전에서는 Visual Studio Code, Eclipse, Theia에 대한 업데이트가 포함되어 있습니다. 주요 기능으로는 Spring Data AOT 리포지토리에 대한 초기 접근 미리보기 지원, Spring Boot 3.5로의 업그레이드 지원, VSCode와 Eclipse에서 계층적 문서 기호 지원 등이 있습니다. 또한, Eclipse 배포판은 2025-06 릴리스로 업데이트되었으며, Java 24 지원이 기본적으로 포함됩니다. 자세한 변경 사항은 릴리스 노트를 참조하시기 바랍니다. Spring Tools는 [공식 웹사이트](https://spring.io/tools/)에서 다운로드할 수 있습니다. 다음 버전인 Spring Tools 4.32.0은 2025년 7월 말에 출시될 예정입니다.
👉 [자세히 보기](https://spring.io/blog/2025/06/11/spring-tools-4-31-0-released)

## 🔹 Docker - Publishing AI models to Docker Hub
이 블로그 글은 AI 모델을 Docker Hub에 게시하는 방법에 대해 설명합니다. Docker Model Runner가 처음 출시되었을 때, Docker Hub에서 Docker가 관리하는 AI 모델을 실행할 수 있는 기능이 내장되어 있어 사용자가 llama3.2나 gemma3 같은 모델을 쉽게 가져와 로컬에서 사용할 수 있었습니다. 이제 Model Runner는 새로운 세 가지 명령어인 tag, push를 지원하여 사용자들이 AI 모델을 Docker Hub에 게시하고 관리할 수 있도록 돕습니다.
👉 [자세히 보기](https://www.docker.com/blog/publish-ai-models-on-docker-hub/)

## 🔹 Java - JEP targeted to JDK 25: 470: PEM Encodings of Cryptographic Objects (Preview)
이 기술 블로그 글은 JDK 25에 목표로 하고 있는 JEP 470에 관한 내용을 다루고 있습니다. JEP 470은 암호화 객체의 PEM 인코딩을 다루는 기능으로, 현재 프리뷰 상태입니다. 이 기능은 암호화된 데이터를 표준화된 형식으로 표현하여 상호운용성을 높이는 것을 목표로 하고 있습니다. 자세한 내용은 제공된 링크를 통해 확인할 수 있습니다.
👉 [자세히 보기](https://inside.java/2025/06/11/jep470-target-jdk25/)

## 🔹 Golang - [ On | No ] syntactic support for error handling
Go 팀이 오류 처리 지원에 대한 계획을 세우고 있다는 내용을 다루고 있는 기술 블로그 글입니다. 이 글에서는 Go 언어의 오류 처리 구문에 대한 지원 여부와 관련된 논의를 소개하고 있습니다.
👉 [자세히 보기](https://go.dev/blog/error-syntax)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
제목: Helm @ KubeCon + CloudNativeCon EU '25  
요약: Helm 팀이 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU '25에 참석합니다. 올해 말 출시 예정인 Helm 4에 대해 논의할 수 있는 기회가 마련되어 있으니, 발표 세션과 Project Pavilion에 있는 Helm 부스에서 유지 관리자들과 함께 이야기에 참여해 보세요. 행사 기간 동안 진행되는 Helm 관련 활동에 대한 자세한 정보는 아래 링크에서 확인할 수 있습니다.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

