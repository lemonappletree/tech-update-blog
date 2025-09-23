# 🛠️ 2025-09-23 기술 업데이트 요약

## 🔹 Kubernetes - Kubernetes v1.34: Pod Level Resources Graduated to Beta
Kubernetes 커뮤니티는 Kubernetes v1.34 버전에서 Pod 레벨 리소스 기능이 베타로 전환되어 기본 활성화되었음을 발표했습니다. 이 기능은 Pod 전체에 대해 CPU 및 메모리 리소스를 정의할 수 있는 유연성을 제공하여, 여러 컨테이너가 포함된 Pod에서 리소스 관리의 복잡성을 줄여줍니다. Pod 레벨 리소스는 컨테이너 레벨과 결합해 정확한 리소스 요구 사항을 표현할 수 있으며, 컨테이너 간에 사용되지 않는 리소스를 공유할 수 있어 효율적인 리소스 활용이 가능합니다. Pod 레벨과 컨테이너 레벨 리소스가 모두 지정된 경우, Pod 레벨 리소스가 우선 적용되며, 이는 클러스터 관리자에게 전체적인 리소스 경계를 설정할 수 있는 강력한 도구를 제공합니다. 현재 이 기능은 CPU, 메모리, 큰 페이지 리소스에만 적용되며, Windows Pod에서는 지원되지 않습니다. Kubernetes v1.34 이상에서 사용 가능하며, 사용자 피드백을 통해 기능 개선에 기여할 수 있습니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/09/22/kubernetes-v1-34-pod-level-resources/)

## 🔹 Spring Boot - Spring AI 1.1.0-M2 Available Now: Enhanced Model Context Protocol Support
Spring AI 1.1.0-M2가 Maven Central을 통해 출시되었습니다. 이번 릴리스는 주로 모델 컨텍스트 프로토콜(MCP) 지원을 강화하는 데 중점을 두었으며, MCP Java SDK v0.13.0의 주요 개선 사항과 Spring AI 생태계 전반에 걸친 업데이트를 포함합니다. 주요 개선 사항으로는 MCP Java SDK의 업데이트, MCP 통합 문제 해결, 새로운 기능 추가, 안정성 향상, 문서 개선 등이 있습니다. 또한, Docker Compose 지원, Testcontainers 통합, VertexAI Gemini 응답 스키마 검증 등의 기능도 포함되어 있습니다. 이 릴리스는 커뮤니티 기여자들의 협력으로 이루어졌으며, 다양한 버그 수정과 기능 개선이 이루어졌습니다.
👉 [자세히 보기](https://spring.io/blog/2025/09/19/spring-ai-1-1-0-M2-mcp-focused)

## 🔹 Docker - Silent Component Updates & Redesigned Update Experience
Docker Desktop의 업데이트 방식을 개선하기 위한 이전의 노력에 이어, Docker Desktop 4.46 버전부터 개발 도구를 최신 상태로 유지하기 위한 자동 구성 요소 업데이트와 완전히 새로워진 업데이트 경험을 도입한다는 내용을 담고 있습니다. 이러한 변화는 사용자 생산성을 우선으로 고려하여 설계되었습니다.
👉 [자세히 보기](https://www.docker.com/blog/docker-desktop-silent-component-updates/)

## 🔹 Java - Paths to Support Additional Numeric Types on the Java Platform #JVMLS
이 기술 블로그 글은 Java 플랫폼에서 추가적인 숫자 타입을 지원하기 위한 경로에 대해 설명하고 있습니다. Java 플랫폼의 숫자 타입은 여러 해 동안 안정적이었지만, 과학 및 공학 계산에서는 선형 대수와 복소수가 중요하고, 머신 러닝에서는 16비트 부동소수점 숫자 등 작은 숫자 타입의 활용이 이점이 있습니다. 심지어 IEEE SA Working Group P3109는 머신 러닝을 위한 8비트 부동소수점 형식을 표준화하는 것을 연구하고 있습니다. 이 글은 Java 플랫폼에서 새로운 숫자 타입을 완전히 지원하기 위해 필요한 요소들을 논의하고, 이를 지원하기 위한 다양한 경로에서의 트레이드오프를 제시합니다.
👉 [자세히 보기](https://inside.java/2025/09/21/jvmls-java-additional-numeric-types/)

## 🔹 Golang - It's survey time! How has Go has been working out for you?
제목: 설문 조사 시간입니다! Go 언어는 여러분에게 어떻게 도움이 되었나요?
요약: Go 언어의 미래를 함께 만들어가세요. 

이 블로그 글은 Go 언어 사용자를 대상으로 한 설문 조사를 소개하며, 사용자들이 설문에 참여함으로써 Go 언어의 발전 방향에 기여할 수 있음을 강조합니다. 설문 조사를 통해 사용자들의 경험과 피드백을 수집하여 Go 언어의 향후 개선에 반영하고자 합니다.
👉 [자세히 보기](https://go.dev/blog/survey2025-announce)

## 🔹 Helm - Path To Releasing Helm v4
Helm v4의 첫 번째 알파 버전이 출시되었습니다. 개발의 마무리 단계에 접어든 Helm v4에 대해 현재 진행 상황과 커뮤니티가 어떻게 참여할 수 있는지를 공유하고자 합니다. 자세한 내용은 링크를 통해 확인할 수 있습니다.
👉 [자세히 보기](https://helm.sh/blog/path-to-helm-v4/)

