# 🛠️ 2025-06-08 기술 업데이트 요약

## 🔹 Kubernetes - Introducing Gateway API Inference Extension
이 블로그 글에서는 Kubernetes에서 생성 AI 및 대규모 언어 모델(LLM) 서비스의 트래픽 라우팅 문제를 해결하기 위해 Gateway API Inference Extension을 소개합니다. 기존 로드 밸런서는 LLM 추론 세션과 같은 장기 실행, 자원 집약적, 부분 상태 유지 작업을 처리하기에 적합하지 않습니다. Gateway API Inference Extension은 이러한 문제를 해결하기 위해 개발되었으며, 모델 인식 라우팅, 요청 중요도 지원, 안전한 모델 롤아웃, 실시간 모델 메트릭 기반 로드 밸런싱 최적화 등을 제공합니다.

이 확장은 두 가지 주요 사용자 정의 리소스를 도입합니다. InferencePool은 모델 서버를 정의하여 일관된 자원 사용을 보장하며, InferenceModel은 사용자에게 모델 엔드포인트를 관리할 수 있게 합니다. 요청 흐름은 게이트웨이와 HTTP 라우트를 기반으로 하며, 추가적인 추론 인식 단계가 포함됩니다. 벤치마크 결과에 따르면 이 확장은 GPU 기반 LLM 작업 부하에서 지연 시간을 크게 줄였습니다.

향후 계획으로는 프리픽스 캐시 인식 로드 밸런싱, 다양한 모델 유형 지원, 이기종 가속기 지원 등이 포함됩니다. Gateway API Inference Extension은 AI/ML 트래픽 라우팅을 표준화하고 간소화하여 운영 팀이 적절한 LLM 서비스를 효율적으로 제공할 수 있도록 돕습니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/06/05/introducing-gateway-api-inference-extension/)

## 🔹 Spring Boot - A Bootiful Podcast: IntelliJ IDEA lead Aleksey Stukalov
이 기술 블로그 글은 Spring 팬들을 대상으로 하며, IntelliJ IDEA의 리더인 Aleksey Stukalov와의 대화를 다루고 있습니다. 글에서는 팟캐스트 형식으로 진행된 인터뷰 내용을 소개하고 있습니다.
👉 [자세히 보기](https://spring.io/blog/2025/06/05/a-bootiful-podcast-aleksey-stukalov)

## 🔹 Docker - Settings Management for Docker Desktop now generally available in the Admin Console
Docker Desktop의 설정 관리 기능이 이제 관리자 콘솔에서 일반적으로 사용할 수 있게 되었습니다. 이 기능은 Docker Business 구독 고객을 위해 관리자 콘솔에서 구성할 수 있으며, 초기 액세스 기간을 성공적으로 마친 후 새로운 컴플라이언스 보고 기능이 추가되었습니다. 이를 통해 중앙 집중식 Docker Desktop 관리에 대한 비전을 완성하게 되었습니다.
👉 [자세히 보기](https://www.docker.com/blog/settings-management-for-docker-desktop-now-generally-available-in-the-admin-console/)

## 🔹 Java - Key Java Language Updates From 2020 to 2025
블로그 글에서는 오라클의 Java Platform Group 멤버이자 Project Amber에 기여한 Gavin Bierman이 2020년부터 2025년까지의 Java 언어 발전을 돌아봅니다. 특히, Java 25에서 최종적으로 도입된 '유연한 생성자 본문'이라는 기능에 초점을 맞추고 있습니다.
👉 [자세히 보기](https://inside.java/2025/06/06/key-java-language-updates/)

## 🔹 Golang - [ On | No ] syntactic support for error handling
이 블로그 글은 Go 팀이 오류 처리에 대한 구문 지원 계획을 논의하는 내용입니다. Go 언어에서의 오류 처리 방식을 개선하기 위한 다양한 아이디어와 그에 따른 계획을 설명하고 있습니다. 현재의 오류 처리 방법을 검토하고, 이를 보다 효율적이고 직관적으로 만들기 위한 방안을 모색하고 있습니다.
👉 [자세히 보기](https://go.dev/blog/error-syntax)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
블로그 글 요약: Helm 팀이 2025년 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU에 참가합니다. 올해 말 출시 예정인 Helm 4에 대한 논의에 참여할 수 있는 기회가 주어집니다. 팀의 발표 세션과 프로젝트 파빌리온 내의 Helm 부스에서 유지 관리자들과의 대화에 참여하세요. 주간 동안 진행되는 Helm 관련 활동에 대한 자세한 내용은 링크를 참조하세요.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

