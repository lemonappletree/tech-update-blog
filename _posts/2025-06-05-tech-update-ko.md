# 🛠️ 2025-06-05 기술 업데이트 요약

## 🔹 Kubernetes - Introducing Gateway API Inference Extension
이 블로그 글은 "Gateway API Inference Extension"의 소개를 다룹니다. 현대의 생성 AI와 대형 언어 모델(LLM) 서비스가 Kubernetes 상에서 고유한 트래픽 라우팅 문제를 일으키는데, 기존의 짧고 무상태인 웹 요청과 달리, LLM 추론 세션은 장기적이고 자원 집약적이며 부분적으로 상태를 유지합니다. 기존의 로드 밸런서는 이러한 워크로드에 필요한 특수 기능을 제공하지 않으며, 모델의 정체성이나 요청의 중요성을 고려하지 않습니다.

"Gateway API Inference Extension"은 이러한 문제를 해결하기 위해 개발되었습니다. 이 확장은 Gateway API에 기반을 두고 있으며, 추론을 위한 특정 라우팅 기능을 추가하여 GenAI/LLM을 "모델-서비스"로서 자체 호스팅할 수 있게 합니다. 이 프로젝트의 목표는 생태계 전반에서 추론 워크로드에 대한 라우팅을 개선하고 표준화하는 것입니다.

추론 확장은 두 개의 새로운 사용자 정의 리소스(CRD)를 도입합니다: InferencePool과 InferenceModel. InferencePool은 모델 서버가 실행되는 포드를 정의하며, 플랫폼 관리자가 배포 및 균형 조정을 관리합니다. InferenceModel은 AI/ML 소유자가 관리하는 모델 엔드포인트로, 공용 이름을 실제 모델에 매핑합니다.

이 확장은 모델 인식 라우팅을 통해 GPU 지원 LLM 워크로드의 지연 시간을 줄이고, 전통적인 로드 밸런싱 방법으로 나타날 수 있는 핫스팟을 피합니다. 향후 계획으로는 프리픽스-캐시 인식 로드 밸런싱, 다양한 모델 유형 지원, 이질적 가속기 지원 등이 포함됩니다. Gateway API Inference Extension은 Kubernetes 네이티브 도구와의 정렬을 통해 AI/ML 트래픽 라우팅을 단순화하고 표준화하는 것을 목표로 합니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/06/05/introducing-gateway-api-inference-extension/)

## 🔹 Spring Boot - This Week in Spring - June 3rd, 2025
이번 주 Spring 블로그 요약 (6월 3일, 2025):

Spring 팬 여러분, 이번 주 Spring 블로그에 오신 것을 환영합니다! IntelliJ IDEA 프로젝트 리더 Aleksey Stukalov과 함께 Java, Kotlin, Spring 개발자를 위한 IntelliJ IDEA의 새로운 기능들에 대해 녹화를 마쳤습니다. Jetbrains 팀에 감사드리며, 내일은 JSpring 컨퍼런스에서 발표를 합니다.

주요 업데이트:
- Spring Cloud 2022.0.11 및 2025.0.0 버전 출시
- Spring Cloud Gateway의 여러 버전 출시 및 보안 취약점 수정
- 'A Bootiful Podcast'에서 Victor Rentea와의 대화
- Spring Modulith의 새로운 릴리스
- Vite Spring Boot 0.9.0 출시
- IntelliJ IDEA에서 Spring Data AOT 저장소 지원 예정
- IntelliJ IDEA의 JPA 엔티티 역공학 지원 예정

자세한 내용은 [블로그 링크](https://spring.io/blog/2025/06/03/this-week-in-spring-june-3rd-2025)에서 확인하세요.
👉 [자세히 보기](https://spring.io/blog/2025/06/03/this-week-in-spring-june-3rd-2025)

## 🔹 Docker - Settings Management for Docker Desktop now generally available in the Admin Console
Docker Desktop의 설정 관리 기능이 이제 관리자 콘솔에서 일반적으로 사용할 수 있게 되었습니다. Docker Business 구독을 가진 고객은 관리자 콘솔에서 설정 관리를 구성할 수 있습니다. 초기 접근 기간을 성공적으로 마친 후, 이 강력한 관리 솔루션은 새로운 규정 준수 보고 기능으로 강화되어 중앙 집중식 Docker Desktop 관리를 위한 비전을 완성했습니다.
👉 [자세히 보기](https://www.docker.com/blog/settings-management-for-docker-desktop-now-generally-available-in-the-admin-console/)

## 🔹 Java - Ubuntu Ships Java, Spring, AOT
이 블로그 글에서는 Ubuntu 커뮤니티 디스코스에 올라온 새로운 게시물(2025년 5월 23일)을 소개하며, Ubuntu 애플리케이션 개발을 지원하는 프로그래밍 도구 체인에 대해 설명합니다. 주요 내용으로는 Ubuntu가 Java, Spring, AOT(Ahead-Of-Time) 컴파일을 포함한 다양한 도구와 기술을 제공하여 개발자들이 더욱 효율적으로 애플리케이션을 개발할 수 있도록 지원한다는 점이 강조되고 있습니다.
👉 [자세히 보기](https://inside.java/2025/06/04/ubuntu-leyden/)

## 🔹 Golang - [ On | No ] syntactic support for error handling
Go 팀이 오류 처리 지원에 대한 계획을 세우고 있다는 내용의 기술 블로그 글입니다. 블로그에서는 Go 언어에서의 오류 처리 구문 지원 여부에 대한 논의가 이루어지고 있으며, 이에 대한 팀의 계획과 방향성이 설명되고 있습니다.
👉 [자세히 보기](https://go.dev/blog/error-syntax)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
제목: Helm @ KubeCon + CloudNativeCon EU '25

Helm 팀이 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU '25에 참가합니다. 올해 말 출시 예정인 Helm 4에 대해 논의할 수 있는 기회가 마련되어 있으며, 발표 세션과 프로젝트 파빌리온 내 Helm 부스에서 유지 관리자들과 함께 대화할 수 있습니다. 주간 동안 진행되는 Helm 관련 활동에 대한 자세한 내용은 아래 링크를 참고하세요.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

