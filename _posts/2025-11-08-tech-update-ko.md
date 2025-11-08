# 🛠️ 2025-11-08 기술 업데이트 요약

## 🔹 Kubernetes - Gateway API 1.4: New Features
이 블로그 글은 Kubernetes Gateway API의 최신 버전 1.4.0의 새로운 기능과 개선 사항을 소개합니다. 이 버전은 Kubernetes의 네트워킹을 현대적이고 확장 가능하게 만들어주는 다양한 기능을 포함하고 있습니다. 주요 업데이트는 다음과 같습니다:

1. **새로운 기능:**
   - **BackendTLSPolicy:** 게이트웨이와 백엔드 간의 TLS 설정을 정의할 수 있는 기능입니다.
   - **supportedFeatures 필드:** GatewayClass 상태에 구현된 기능 목록을 포함하여 사용자가 지원되는 기능을 명확히 이해할 수 있게 합니다.
   - **Routes에 이름 지정 규칙:** 특정 규칙을 명확히 식별하고 참조할 수 있게 합니다.

2. **실험적 기능:**
   - **Mesh 리소스:** 서비스 메쉬 구성에 대한 지원을 제공합니다.
   - **기본 게이트웨이:** 구성 부담을 줄여주는 기능입니다.
   - **HTTPRoute에 대한 외부 인증 필터:** 외부 서비스에 요청을 인증 및 권한 부여할 수 있는 필터입니다.

3. **기타 업데이트:**
   - **TLS 설정 개선:** 각 포트별 TLS 설정을 통해 보안을 강화합니다.
   - **개발 경험 개선:** API 리뷰어의 부담을 줄이고 일반적인 실수를 줄이기 위한 개선 사항이 포함되었습니다.

이외에도 API 사용 경험을 향상시키기 위한 문서 개선 작업이 진행되었습니다. Kubernetes 1.26 이상에서 이 버전을 사용할 수 있으며, 다양한 구현체가 이미 이 버전을 지원하고 있습니다. 커뮤니티에 참여하여 Gateway API의 발전에 기여할 수도 있습니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/11/06/gateway-api-v1-4/)

## 🔹 Spring Boot - A Bootiful Podcast: The Vaadin team, live from Vaadin Create 2025
이 기술 블로그 글은 "A Bootiful Podcast"라는 제목으로, 2025년 독일 프랑크푸르트에서 열린 Vaadin Create 행사에서 Vaadin의 전설적인 인물들인 Joonas Lehtinen, Marcus Hellberg, Leif Åstrand와 함께한 인터뷰 내용을 다루고 있습니다. 이 팟캐스트는 스프링 팬들에게 Vaadin 팀과의 특별한 대화를 제공합니다.
👉 [자세히 보기](https://spring.io/blog/2025/11/06/a-bootiful-podcasd-vaadin-team)

## 🔹 Docker - Most DevSecOps Advice Is Useless without Context—Here’s What Actually Works
기술 블로그 글 요약: 일반적인 DevSecOps 조언은 문서상으로는 좋아 보이지만, 팀의 맥락, 워크플로우, 환경에 맞춘 요구 사항을 무시하기 때문에 실제로는 잘 작동하지 않는 경우가 많습니다. 과도한 통제, 광범위한 정책, 잘못 적용된 도구는 개발 흐름을 방해하며, 흐름이 깨지면 보안 조치가 가장 먼저 무시됩니다. 앞으로 나아가기 위해서는 더 많은 규칙이 아니라, 더 스마트한 접근 방식이 필요합니다.
👉 [자세히 보기](https://www.docker.com/blog/context-aware-devsecops-what-works/)

## 🔹 Java - JEP targeted to JDK 26: 500: Prepare to Make Final Mean Final
이 기술 블로그 글은 JDK 26을 목표로 하는 JEP 500에 관한 내용을 다루고 있습니다. JEP 500의 주요 내용은 'final' 키워드의 의미를 강화하여, 'final'로 선언된 요소가 정말로 변경 불가능하도록 준비하는 것입니다. 이를 통해 Java 언어의 일관성을 높이고, 개발자들이 'final' 키워드를 사용할 때 더욱 신뢰할 수 있도록 하는 것을 목표로 하고 있습니다.
👉 [자세히 보기](https://inside.java/2025/11/07/jep500-target-jdk26/)

## 🔹 Golang - The Green Tea Garbage Collector
블로그 글은 Go 1.25에 새롭게 도입된 실험적인 가비지 컬렉터인 "Green Tea"에 대해 다루고 있습니다. 이 가비지 컬렉터는 메모리 관리 효율성을 개선하기 위해 설계되었으며, Go 언어의 성능 향상을 목표로 합니다. "Green Tea" 가비지 컬렉터의 주요 특징과 작동 방식에 대한 설명이 포함되어 있습니다.
👉 [자세히 보기](https://go.dev/blog/greenteagc)

