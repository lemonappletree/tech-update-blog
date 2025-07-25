# 🛠️ 2025-07-25 기술 업데이트 요약

## 🔹 Kubernetes - Post-Quantum Cryptography in Kubernetes
이 블로그 글은 양자 컴퓨팅의 발전으로 인해 암호 기술이 직면한 주요 변화에 대해 설명하고 있습니다. 현재의 암호 표준이 양자 컴퓨터에 의해 깨질 수 있는 가능성이 우려되는 상황에서, Post-Quantum Cryptography(PQC)가 이에 대한 대안으로 떠오르고 있습니다. 글에서는 TLS와 Kubernetes 생태계에 PQC가 미치는 영향을 다루며, 특히 TLS의 두 가지 주요 암호화 작업인 키 교환과 디지털 서명에 대해 설명합니다.

PQC 알고리즘은 양자 및 고전 컴퓨터 모두에 대한 공격에 안전하다고 여겨지며, NIST에서 표준화 작업이 진행 중입니다. Kubernetes에서는 Go 언어로 인해 PQC가 자연스럽게 도입되고 있으며, 최신 버전에서는 하이브리드 키 교환 메커니즘인 `X25519MLKEM768`이 기본적으로 지원됩니다. 그러나 Go 버전 불일치와 같은 잠재적인 문제도 존재합니다.

디지털 서명의 경우 PQC의 도입이 더딘 편이며, 키와 서명 크기가 크고 성능 저하가 발생할 수 있습니다. PQC 서명 표준은 아직 널리 통합되지 않았으며, 실험적인 단계에 있습니다.

결론적으로, Kubernetes는 양자 보안으로의 전환을 진행 중이며, 특히 키 교환에서는 이미 하이브리드 PQC가 적용되고 있습니다. 그러나 디지털 서명과 인증서 계층에서의 PQC 도입은 여전히 초기 단계에 있습니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/07/18/pqc-in-k8s/)

## 🔹 Spring Boot - A Bootiful Podcast: José Paumard, Java developer advocate and professor
블로그 글 요약: 이 글에서는 Devoxx UK 2025에서 녹음된 팟캐스트를 소개하며, 저명한 컴퓨터 과학 교수이자 Java 개발자 옹호자인 José Paumard와 Java 및 그 생태계에 대해 이야기합니다.
👉 [자세히 보기](https://spring.io/blog/2025/07/24/a-bootiful-podcast-jose-paumard)

## 🔹 Docker - Docker MCP Catalog: Finding the Right AI Tools for Your Project
이 기술 블로그 글은 Docker의 MCP(Model Context Protocol) 카탈로그에 대해 설명합니다. LLM(대규모 언어 모델)이 발전하면서 외부 도구와 안전하게 상호작용할 수 있는 표준화된 방법의 필요성이 커지고 있습니다. MCP는 이러한 필요를 충족하기 위해 고안된 프로토콜로, 기존의 API를 AI가 접근 가능한 도구로 변환하는 역할을 합니다. 이 블로그는 AI 프로젝트에 적합한 도구를 찾는 데 있어 MCP 카탈로그가 어떤 도움을 줄 수 있는지 설명합니다.
👉 [자세히 보기](https://www.docker.com/blog/finding-the-right-ai-developer-tools-mcp-catalog/)

## 🔹 Java - A Sneak Peek at the Stable Values API
이 기술 블로그 글은 Java의 일부 내부 JDK 클래스가 `@Stable` 애노테이션에 의존하여 성능, 에너지 효율성, 유연성의 이점을 얻고 있다는 내용을 다룹니다. 그러나 `@Stable` 애노테이션은 Java 애플리케이션에서 직접 사용할 수 없어 그 활용이 제한적이었습니다. StableValue API는 이러한 불균형을 해결하여 `@Stable` 애노테이션을 감싸는 안전한 래퍼를 제공함으로써 일반 Java 개발자와 서드파티 라이브러리 개발자들이 그 이점을 활용할 수 있게 합니다. 이 API를 통해 요소가 상수 값인 것처럼 높은 성능을 가진 지연 초기화 리스트와 맵을 생성하는 방법을 배울 수 있습니다.
👉 [자세히 보기](https://inside.java/2025/07/22/javaone-stablevalues/)

## 🔹 Golang - The FIPS 140-3 Go Cryptographic Module
제목: FIPS 140-3 Go 암호 모듈  
요약: Go 언어에 이제 내장된 FIPS 140-3 호환 모드가 추가되었습니다.  
링크: [Go 블로그](https://go.dev/blog/fips140)
👉 [자세히 보기](https://go.dev/blog/fips140)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
블로그 글 요약: Helm 팀이 2025년 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU '25에 참가합니다. 올해 말 출시 예정인 Helm 4에 대한 논의가 진행될 예정이니, 발표 세션과 프로젝트 파빌리온에 있는 Helm 부스에서 유지 보수자들과의 대화에 참여하세요. 주간 동안 진행되는 Helm 관련 활동에 대한 자세한 내용은 링크를 참고하세요.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

