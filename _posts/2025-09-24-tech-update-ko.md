# 🛠️ 2025-09-24 기술 업데이트 요약

## 🔹 Kubernetes - Kubernetes v1.34: Pod Level Resources Graduated to Beta
이 기술 블로그 글은 Kubernetes v1.34에서 Pod 레벨 자원 기능이 베타로 승격되었음을 발표하는 내용입니다. 이 기능은 Pod 전체에 대한 CPU와 메모리 자원을 지정할 수 있게 하여 자원 할당에 유연성을 제공합니다. 이전에는 개별 컨테이너 수준에서만 자원을 지정할 수 있었으나, 이제는 Pod 전체에 대해 자원 요청과 제한을 설정할 수 있어 관리가 더 쉬워졌습니다. Pod 레벨 자원은 컨테이너들이 남는 자원을 공유할 수 있게 하여 자원 사용 효율성을 높입니다. 이 기능은 Pod의 QoS 클래스에 영향을 주고, 리눅스 노드에서는 OOM 점수 조정 시 고려됩니다. Kubernetes v1.34 이상에서 이 기능을 사용하려면 PodLevelResources 기능 게이트를 활성화해야 합니다. Pod 레벨 자원은 CPU, 메모리, hugepages만 지원하며, Windows Pod에는 적용되지 않습니다. Pod 레벨 자원 기능이 베타 단계에 있으므로 사용자 피드백이 중요합니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/09/22/kubernetes-v1-34-pod-level-resources/)

## 🔹 Spring Boot - This Week in Spring - September 23rd, 2025
이번 주 Spring 블로그 글은 다양한 행사 준비와 함께 커뮤니티의 여러 소식을 다루고 있습니다. Spring Framework 7의 새로운 HTTP 서비스 클라이언트 기능, Spring AI 1.0.2의 향상된 MCP 지원, Spring Modulith 2.0 M3 출시, Spring Boot 3.4.10, 3.5.6, 4.0.0 M3 버전 출시, Spring AI 1.0.2, Spring Batch 6.0.0 M3 및 5.2.3, Spring Integration 7.0 M3, Spring for Apache Kafka 4.0.0-M5 출시 소식이 포함되어 있습니다. 또한, Spring 웹 애플리케이션에서 멀티파트 데이터를 스트리밍하는 방법, Java와 Spring을 사용한 간단한 규칙 엔진 구현, 통합 테스트 최적화 기사, Spring 설립자 Rod Johnson과 Juergen Hoeller의 재회, JRuby에서 Spring Boot 애플리케이션 실행 등 다양한 주제가 다뤄졌습니다.
👉 [자세히 보기](https://spring.io/blog/2025/09/23/this-week-in-spring-september-23rd-2025)

## 🔹 Docker - MCP Horror Stories: The Drive-By Localhost Breach
이 블로그 글은 "MCP 공포 이야기" 시리즈의 네 번째 부분으로, AI 인프라의 심각한 취약점을 드러낸 실제 보안 사고를 분석하고, Docker MCP Gateway가 어떻게 정교한 공격 벡터에 대한 기업 수준의 보호를 제공하는지를 설명합니다. Model Context Protocol (MCP)은 개발자들이 AI 에이전트를 개발 환경에 통합하는 방식을 혁신적으로 변화시켰으며, 이 글에서는 그와 관련된 보안 사건과 해결책을 다룹니다.
👉 [자세히 보기](https://www.docker.com/blog/mpc-horror-stories-cve-2025-49596-local-host-breach/)

## 🔹 Java - JavaFX 25 Highlights
JavaFX 25가 출시되어 여러 새로운 기능과 개선 사항을 제공합니다. 이 버전은 JDK 25와 함께 사용하도록 설계되었으며, JDK 23 이후 버전과 호환됩니다.
👉 [자세히 보기](https://inside.java/2025/09/23/javafx-25/)

## 🔹 Golang - It's survey time! How has Go has been working out for you?
기술 블로그 글 요약: "Go 언어의 미래를 함께 만들어가요! Go 언어 사용자 설문조사에 참여하여 여러분의 경험과 의견을 공유해 주세요. 이번 설문조사는 Go 언어의 발전 방향을 결정하는 데 중요한 역할을 할 것입니다."
👉 [자세히 보기](https://go.dev/blog/survey2025-announce)

## 🔹 Helm - Path To Releasing Helm v4
**요약:** Helm v4의 첫 번째 알파 버전이 출시되었습니다. Helm v4 개발이 막바지에 이르렀고, 이번 블로그 글에서는 현재 진행 상황과 더 넓은 커뮤니티가 어떻게 참여할 수 있는지에 대한 세부 사항을 공유하고자 합니다.
👉 [자세히 보기](https://helm.sh/blog/path-to-helm-v4/)

