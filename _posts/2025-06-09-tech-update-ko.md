# 🛠️ 2025-06-09 기술 업데이트 요약

## 🔹 Kubernetes - Introducing Gateway API Inference Extension
이 기술 블로그 글에서는 Kubernetes에서 발생하는 생성 AI 및 대형 언어 모델(LLM) 서비스의 트래픽 라우팅 문제를 해결하기 위해 개발된 "Gateway API Inference Extension"을 소개합니다. 기존의 HTTP 경로 중심 로드 밸런서는 이러한 작업에 필요한 특화된 기능이 부족합니다. 이 확장은 기존의 Gateway API에 추론 특화 라우팅 기능을 추가하여, AI/ML 작업의 라우팅을 개선하고 표준화하는 것을 목표로 합니다. 

Inference Gateway는 모델 인식 라우팅, 요청 중요도 지원, 안전한 모델 롤아웃, 실시간 모델 메트릭스를 기반으로 한 로드 밸런싱을 통해 AI 작업의 지연 시간을 줄이고 GPU 활용도를 높입니다. 이 확장은 'InferencePool'과 'InferenceModel'이라는 두 가지 새로운 사용자 정의 리소스를 도입하여 AI/ML 워크플로우를 효과적으로 관리할 수 있게 도와줍니다. 

벤치마크 결과에 따르면, 이 확장은 GPU 기반 LLM 작업에서 전통적인 로드 밸런싱 방법에 비해 지연 시간을 크게 줄이는 것으로 나타났습니다. 로드맵에는 원격 캐시를 위한 프리픽스 캐시 인식 로드 밸런싱, 대규모 다중 모달 입력/출력 지원 등 다양한 기능이 계획되어 있습니다. Gateway API Inference Extension은 Kubernetes 도구와의 정렬을 통해 AI/ML 트래픽 라우팅을 단순화하고 표준화하는 것을 목표로 합니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/06/05/introducing-gateway-api-inference-extension/)

## 🔹 Spring Boot - A Bootiful Podcast: IntelliJ IDEA lead Aleksey Stukalov
제목: 아름다운 팟캐스트: IntelliJ IDEA 리더 Aleksey Stukalov

요약: 안녕하세요, Spring 팬 여러분! 이번 에피소드에서는 IntelliJ IDEA의 리더 Aleksey Stukalov와 대화를 나눕니다.
👉 [자세히 보기](https://spring.io/blog/2025/06/05/a-bootiful-podcast-aleksey-stukalov)

## 🔹 Docker - Settings Management for Docker Desktop now generally available in the Admin Console
Docker Desktop의 설정 관리 기능이 이제 관리자 콘솔에서 일반적으로 사용 가능하게 되었습니다. Docker Business 구독을 가진 고객은 관리자 콘솔에서 설정 관리 기능을 구성할 수 있습니다. 초기 액세스 기간 이후, 이 강력한 관리 솔루션은 새로운 준수 보고 기능으로 강화되어 중앙 집중식 Docker Desktop 관리에 대한 비전을 완성했습니다.
👉 [자세히 보기](https://www.docker.com/blog/settings-management-for-docker-desktop-now-generally-available-in-the-admin-console/)

## 🔹 Java - Key Java Language Updates From 2020 to 2025
이 블로그 글은 Oracle의 Java 플랫폼 그룹 멤버이자 Project Amber의 기여자인 Gavin Bierman이 2020년부터 2025년까지의 Java 언어 개발을 되돌아보는 내용을 담고 있습니다. 특히 Java 25에서 최종 확정된 유연한 생성자 본문(flexible constructor bodies) 기능에 중점을 두고 있습니다.
👉 [자세히 보기](https://inside.java/2025/06/06/key-java-language-updates/)

## 🔹 Golang - [ On | No ] syntactic support for error handling
이 기술 블로그 글에서는 Go 팀이 오류 처리에 대한 구문 지원을 어떻게 계획하고 있는지를 다루고 있습니다. Go 언어 내에서 오류 처리의 중요성을 인식하고 있으며, 이를 개선하기 위한 다양한 접근 방식을 고려하고 있습니다. 구체적인 구현 방안이나 방향성에 대한 논의가 포함되어 있습니다.
👉 [자세히 보기](https://go.dev/blog/error-syntax)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
블로그 글 요약: Helm 팀은 2025년 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU에 참가합니다. 올해 말 출시 예정인 Helm 4에 대한 대화에 참여할 수 있는 기회이니, 발표 세션과 프로젝트 파빌리온에 있는 Helm 부스에서 유지보수자들과 함께하세요. 주간 동안의 모든 Helm 관련 활동에 대한 자세한 내용은 링크를 통해 확인할 수 있습니다.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

