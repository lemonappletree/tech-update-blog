# 🛠️ 2025-06-17 기술 업데이트 요약

## 🔹 Kubernetes - Changes to Kubernetes Slack
Kubernetes Slack은 특별한 지위를 잃고 6월 20일부터 표준 무료 Slack으로 변경됩니다. 이후 올해 말까지 커뮤니티는 새로운 플랫폼으로 이동할 가능성이 큽니다. 채널이나 비공개 채널을 관리하거나 사용자 그룹의 멤버인 경우, 즉시 조치를 취해야 할 필요가 있습니다.

지난 10년 동안 Slack은 무료 맞춤형 엔터프라이즈 계정을 통해 Kubernetes 프로젝트를 지원해왔으나, 이제 더 이상 지원할 수 없음을 알렸습니다. 이에 따라 Slack은 표준 무료 버전으로 다운그레이드되며, 커뮤니티는 다른 대안을 모색하고 구현할 예정입니다.

6월 20일부터 무료 Slack의 기능 제한이 적용되며, 90일의 기록만 유지되고 현재 사용 중인 여러 앱과 워크플로우를 비활성화해야 합니다. Slack 관리자 팀은 이러한 제한을 최대한 잘 관리할 것입니다.

책임 있는 채널 소유자, 비공개 채널의 멤버, 사용자 그룹의 멤버는 업그레이드에 대비하고 정보를 보존하기 위한 조치를 취해야 합니다. CNCF 프로젝트 직원은 커뮤니티가 Discord로의 마이그레이션을 검토할 것을 제안했습니다. Discord는 커뮤니티에 도움을 줄 새로운 도구와 통합 기능을 구현할 수 있게 하며, 스티어링 커미티는 향후 플랫폼을 논의하고 결정할 것입니다.

자세한 내용은 FAQ를 참조하고, kubernetes-dev 메일링 리스트 및 #announcements 채널에서 추가 소식을 확인하세요. Slack 상태에 대한 특정 피드백은 GitHub 토론에 참여하세요.
👉 [자세히 보기](https://kubernetes.io/blog/2025/06/16/changes-to-kubernetes-slack/)

## 🔹 Spring Boot - Spring Vault 4.0.0-M1 available
Spring Vault 4.0.0-M1 마일스톤 릴리스가 발표되었습니다. 주요 기능으로는 Spring Framework 7.0 M6, Kotlin 2.2-RC1, JSpecify 1.0으로의 업그레이드, Jackson 3 및 Jackson 2 지원, Reactor, Jetty, JDK HTTP 클라이언트에 대한 지원 등이 포함됩니다. 자세한 내용 및 업그레이드 방법은 릴리스 노트를 참조하세요. 기여한 모든 분들께 감사드리며, 전체 변경 사항은 GitHub에서 확인할 수 있습니다.
👉 [자세히 보기](https://spring.io/blog/2025/06/16/spring-vault-4-0-0-m1-available)

## 🔹 Docker - How to Build, Run, and Package AI Models Locally with Docker Model Runner
이 기술 블로그 글은 AI 모델을 로컬 환경에서 실행하고 패키징하는 방법을 설명합니다. 저자는 Senior DevOps 엔지니어이자 Docker Captain으로서 다양한 분야의 AI 시스템 개발 경험을 바탕으로, AI 기능이 현대 인프라의 핵심임을 강조합니다. 이 가이드는 Docker Model Runner라는 경량의 개발자 친화적인 도구를 사용하여 AI 모델을 로컬에서 실행하고 패키징하는 방법을 소개합니다.
👉 [자세히 보기](https://www.docker.com/blog/how-to-build-run-and-package-ai-models-locally-with-docker-model-runner/)

## 🔹 Java - Quality Outreach Heads-up - JDK 25: Changes in Some File Operation Behaviors on Windows
이 기술 블로그 글은 JDK 25에 포함된 Windows의 파일 작업 동작 변경 사항에 대한 내용을 다루고 있습니다. 주요 변경 사항으로는 파일 삭제와 경로 처리에 대한 더 엄격한 규칙이 포함됩니다. 이 글은 관련 프로젝트에 정기적으로 전달되는 소통의 일환으로 작성되었습니다.
👉 [자세히 보기](https://inside.java/2025/06/16/quality-heads-up/)

## 🔹 Golang - [ On | No ] syntactic support for error handling
제목: [ On | No ] 구문 지원을 통한 오류 처리  
요약: Go 팀은 오류 처리 지원에 대한 계획을 세우고 있습니다.  
링크: https://go.dev/blog/error-syntax

이 글은 Go 언어에서의 오류 처리 구문 지원에 대한 Go 팀의 계획과 논의를 다루고 있습니다. Go 팀은 오류 처리를 보다 효율적이고 명확하게 하기 위한 방법을 모색하며, 새로운 구문 도입을 고려하고 있는 상황입니다. 이와 관련하여 커뮤니티의 피드백도 중요하게 반영하고 있습니다.
👉 [자세히 보기](https://go.dev/blog/error-syntax)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
블로그 글 요약: Helm 팀이 2025년 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU에 참가합니다. 올해 말 출시 예정인 Helm 4와 관련된 대화에 참여할 수 있는 기회가 주어지며, 프로젝트 파빌리온에 위치한 Helm 부스에서도 관련 정보를 얻을 수 있습니다. 행사 주간 동안 진행되는 Helm 관련 활동에 대한 자세한 내용은 블로그에서 확인할 수 있습니다.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

