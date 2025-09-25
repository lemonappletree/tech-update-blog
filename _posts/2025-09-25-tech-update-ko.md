# 🛠️ 2025-09-25 기술 업데이트 요약

## 🔹 Kubernetes - Kubernetes v1.34: Pod Level Resources Graduated to Beta
이 기술 블로그 글은 Kubernetes v1.34에서 "Pod Level Resources" 기능이 베타로 승격되어 기본적으로 활성화되었음을 알리고 있습니다. 이 기능은 Pod 전체에 대한 CPU와 메모리 자원을 정의하고 관리할 수 있는 유연성을 제공하여 여러 컨테이너가 포함된 Pod의 자원 관리를 단순화합니다. Pod 수준의 자원 명세는 컨테이너 수준 명세와 결합하여 애플리케이션의 정확한 자원 요구 사항과 한계를 표현할 수 있습니다. Pod의 모든 컨테이너가 자원을 공유할 수 있어 효율적인 활용이 가능하며, Pod 전체의 자원 요청과 한계가 우선 적용됩니다. 이 기능은 리눅스 노드에서 OOM 점수 조정에도 영향을 미치며, Kubernetes의 기존 기능과 호환되도록 설계되었습니다. 다만, pod-level 자원의 in-place resize는 v1.34에서 지원되지 않으며, Windows pod에 대한 지원도 없습니다. 이 기능을 사용하려면 Kubernetes v1.34 이상이 필요하며, 사용자의 피드백이 중요합니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/09/22/kubernetes-v1-34-pod-level-resources/)

## 🔹 Spring Boot - This Week in Spring - September 23rd, 2025
이번 주 Spring 블로그에서는 다가오는 여러 컨퍼런스에 대한 준비와 함께 커뮤니티의 다양한 소식을 다루고 있습니다. 주요 내용은 다음과 같습니다:

- Spring Framework 7에서 새롭게 추가된 HTTP 서비스 클라이언트 기능 소개
- Spring AI 1.0.2의 출시와 MCP 지원 개선
- Spring Modulith 2.0 M3 출시로 JPA, Jackson 3 지원 등의 업데이트
- Spring Boot 3.4.10, 3.5.6, 4.0.0 M3 버전 출시
- Spring Batch 6.0.0 M3, 5.2.3 버전 출시
- Spring Integration 7.0 M3, Spring for Apache Kafka 4.0.0-M5 출시
- 스트리밍 멀티파트 데이터, 간단한 규칙 엔진 구현, 통합 테스트 최적화에 관한 유용한 자료 소개
- Spring 공동 창업자 Rod Johnson과 Juergen Hoeller의 재회 세션
- JRuby를 사용한 Spring Boot 애플리케이션 실행 시연

이 외에도 다양한 자료와 토론이 포함되어 있습니다.
👉 [자세히 보기](https://spring.io/blog/2025/09/23/this-week-in-spring-september-23rd-2025)

## 🔹 Docker - MCP Horror Stories: The Drive-By Localhost Breach
이 기술 블로그 글은 MCP 공포 이야기 시리즈의 네 번째 부분으로, AI 인프라의 심각한 취약점을 드러내는 실제 보안 사건을 분석합니다. 특히, 개발자들이 AI 에이전트를 개발 환경에 통합하는 방식을 혁신한 모델 컨텍스트 프로토콜(MCP)에 초점을 맞추고 있습니다. 이 글에서는 복잡한 공격 벡터에 대해 엔터프라이즈급 보호를 제공하는 Docker MCP Gateway의 역할을 강조하며, 보안 강화의 중요성을 설명합니다.
👉 [자세히 보기](https://www.docker.com/blog/mpc-horror-stories-cve-2025-49596-local-host-breach/)

## 🔹 Java - JDK 25 Security Enhancements
블로그 글 제목은 "JDK 25 보안 강화"이며, JDK 25가 2025년 9월 16일에 출시되었다는 소식을 전합니다. 이 글에서는 JDK 25의 가장 흥미롭고 유용한 보안 강화 기능들을 소개하고, 이를 암호화, TLS 등 적절한 카테고리로 분류하여 각 분야에서 어떤 변화가 있었는지를 쉽게 찾아볼 수 있도록 정리했습니다.
👉 [자세히 보기](https://inside.java/2025/09/24/jdk25-security-enhancements/)

## 🔹 Golang - It's survey time! How has Go has been working out for you?
제목: 설문 조사 시간입니다! Go 언어가 어떻게 작동하고 있나요?
요약: Go 언어의 미래를 함께 만들어 가는데 도움을 주세요.
링크: [설문 조사 페이지](https://go.dev/blog/survey2025-announce)

블로그 글은 Go 언어 사용 경험에 대한 설문 조사를 통해 사용자들의 의견을 수집하고, 이를 바탕으로 Go 언어의 발전 방향을 결정하는데 기여하고자 하는 내용을 담고 있습니다. 사용자들이 설문에 참여함으로써 Go 커뮤니티의 성장을 돕고, 더 나은 언어로 발전시킬 수 있도록 지원해 달라는 요청이 포함되어 있습니다.
👉 [자세히 보기](https://go.dev/blog/survey2025-announce)

## 🔹 Helm - Path To Releasing Helm v4
제목: Helm v4 출시를 향한 여정

요약: Helm v4의 첫 번째 알파 버전이 출시되었습니다. Helm v4 개발이 마무리 단계에 접어들면서, 현재 진행 상황과 더 넓은 커뮤니티가 어떻게 참여할 수 있는지에 대한 세부 사항을 공유하고자 합니다.
👉 [자세히 보기](https://helm.sh/blog/path-to-helm-v4/)

