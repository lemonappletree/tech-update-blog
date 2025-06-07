# 🛠️ 2025-06-07 기술 업데이트 요약

## 🔹 Kubernetes - Introducing Gateway API Inference Extension
이 블로그 글은 Kubernetes에서 발생하는 생성 AI와 대형 언어 모델(LLM) 서비스의 트래픽 라우팅 문제를 해결하기 위해 소개된 "Gateway API Inference Extension"에 대해 설명합니다. LLM 추론 세션은 긴 시간 동안 실행되며 자원을 많이 소모하고 부분적으로 상태를 유지하기 때문에, 기존의 HTTP 경로나 라운드 로빈 로드 밸런서는 이러한 워크로드에 적합하지 않습니다. 이 확장은 기존 Gateway API에 추론 전용 라우팅 기능을 추가하여, 사용자가 GenAI/LLM을 "서비스로서의 모델" 개념으로 자체 호스팅할 수 있도록 합니다. 주요 기능으로는 모델 인식 라우팅, 요청 중요도 지원, 안전한 모델 롤아웃, 실시간 모델 메트릭 기반 로드 밸런싱 최적화 등이 있습니다. 이러한 기능을 통해 AI 워크로드의 지연 시간을 줄이고 GPU 사용을 개선하는 것을 목표로 합니다. 이 확장은 Kubernetes-native 도구와 일치하여 AI/ML 트래픽 라우팅을 간소화하고 표준화하는 것을 목표로 하며, 모델 인식 라우팅과 중요도 기반 우선 순위를 통해 올바른 LLM 서비스를 적시에 제공할 수 있도록 돕습니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/06/05/introducing-gateway-api-inference-extension/)

## 🔹 Spring Boot - A Bootiful Podcast: IntelliJ IDEA lead Aleksey Stukalov
이번 블로그 글에서는 Spring 팬들을 위해 IntelliJ IDEA의 책임자인 Aleksey Stukalov와의 대화를 소개합니다.
👉 [자세히 보기](https://spring.io/blog/2025/06/05/a-bootiful-podcast-aleksey-stukalov)

## 🔹 Docker - Settings Management for Docker Desktop now generally available in the Admin Console
Docker Desktop의 설정 관리 기능이 이제 관리자 콘솔에서 일반적으로 제공됩니다. Docker Business 구독을 가진 고객은 관리자 콘솔에서 설정 관리 기능을 구성할 수 있습니다. 초기 접근 기간을 성공적으로 마친 후, 이 강력한 관리 솔루션은 새로운 컴플라이언스 보고 기능이 추가되어 Docker Desktop을 중앙에서 관리하려는 우리의 비전을 완성했습니다.
👉 [자세히 보기](https://www.docker.com/blog/settings-management-for-docker-desktop-now-generally-available-in-the-admin-console/)

## 🔹 Java - Key Java Language Updates From 2020 to 2025
이 기술 블로그 글은 오라클의 Java Platform Group의 일원인 Gavin Bierman이 2020년부터 2025년까지의 Java 언어 개발에 대해 다루고 있습니다. 특히, Java 25에서 최종 확정된 기능인 유연한 생성자 본문(flexible constructor bodies)에 초점을 맞추고 있습니다.
👉 [자세히 보기](https://inside.java/2025/06/06/key-java-language-updates/)

## 🔹 Golang - [ On | No ] syntactic support for error handling
이 블로그 글은 Go 팀의 오류 처리 지원 계획에 대한 내용을 다루고 있습니다. Go 언어에서의 오류 처리 구문 지원 여부에 대한 논의와 관련된 정보가 포함되어 있습니다.
👉 [자세히 보기](https://go.dev/blog/error-syntax)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
블로그 글 요약: Helm 팀이 2025년 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU에 참여합니다. 올해 말 출시 예정인 Helm 4에 대한 논의가 진행될 예정이며, 참가자들은 발표 세션과 Helm 부스에서 유지보수자들과 대화를 나눌 수 있습니다. 주간 동안 진행될 모든 Helm 관련 활동에 대한 자세한 내용은 블로그에서 확인할 수 있습니다.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

