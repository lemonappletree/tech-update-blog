# 🛠️ 2025-09-17 기술 업데이트 요약

## 🔹 Kubernetes - Kubernetes v1.34: Moving Volume Group Snapshots to v1beta2
Kubernetes v1.34 버전에서는 볼륨 그룹 스냅샷 기능이 v1beta2로 이동했습니다. 이 기능은 Kubernetes 1.27에서 알파(Alpha) 기능으로 처음 도입된 후, 1.32 버전에서 베타(Beta)로 전환되었습니다. 이 스냅샷 기능은 여러 볼륨에 대해 충돌 일관성을 가진 스냅샷을 생성할 수 있도록 하며, 새 볼륨으로 복원하여 워크로드를 복구할 수 있게 합니다. v1beta2에서는 VolumeSnapshotInfo 구조체가 추가되어, 각 볼륨 스냅샷의 정보를 포함하고 있습니다. 기존 v1beta1 API 객체는 변환 웹훅을 통해 v1beta2 API 객체로 변환됩니다. 이 기능은 CSI 볼륨 드라이버에서만 지원됩니다. 향후 피드백과 채택에 따라 일반 가용성(GA)으로 출시될 계획입니다. 추가 정보는 관련 디자인 사양, 코드 저장소 및 CSI 문서를 통해 확인할 수 있습니다. Kubernetes 프로젝트에 기여하고 싶다면 SIG Storage에 참여할 수 있습니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/09/16/kubernetes-v1-34-volume-group-snapshot-beta-2/)

## 🔹 Spring Boot - This Week in Spring - September 16th, 2025
이번 주 스프링 기술 블로그에서는 Java 25와 GraalVM 25의 출시를 기념하며 새로운 기능들을 소개하고 있습니다. Java 25에서는 모듈 가져오기 선언과 자바 스크립트 지원 등 다양한 기능이 추가되었습니다. 특히, 스크립트 파일에서 단순한 코드로 프로그램을 실행할 수 있게 되었습니다. 또한, AOT(사전 컴파일) 지원이 강화되어 빠른 네이티브 메서드 실행이 가능합니다. 

이번 주 스프링 관련 소식으로는 Spring for GraphQL, Spring AI, Spring Security 등의 다양한 업데이트와 릴리스가 포함되어 있습니다. 특히 Spring AI는 새로운 MCP 지원을 발표했습니다. 또한, Spring Framework와 Spring Security에서 보안 수정을 포함한 여러 릴리스가 진행되었습니다. 

블로그에서는 새로운 기능과 업데이트에 대한 다양한 링크를 제공하고 있으며, SDKMAN.io를 통해 쉽게 버전을 업그레이드할 수 있다고 언급하고 있습니다.
👉 [자세히 보기](https://spring.io/blog/2025/09/16/this-week-in-spring-september-16th-2025)

## 🔹 Docker - MCP Security: A Developer’s Guide
"Model Context Protocol (MCP): 개발자를 위한 가이드"라는 제목의 기술 블로그 글은, Anthropic이 2024년 11월에 MCP를 출시한 이후로 이 프로토콜이 AI 에이전트와 그들이 사용하는 도구, API, 데이터 간의 연결을 담당하는 중요한 요소로 빠르게 자리잡았다는 내용을 다룹니다. 간단한 설정만으로 에이전트가 코드 검색, 티켓 발행, SaaS 시스템 쿼리, 배포 작업 등을 수행할 수 있습니다.
👉 [자세히 보기](https://www.docker.com/blog/mcp-security-explained/)

## 🔹 Java - The Arrival of Java 25
Oracle은 개발자, 기업 및 최종 사용자들을 위해 JDK 25의 일반 공급을 시작했다고 발표했습니다.
👉 [자세히 보기](https://inside.java/2025/09/16/the-arrival-of-java-25/)

## 🔹 Golang - It's survey time! How has Go has been working out for you?
제목: 설문 조사 시간입니다! Go 언어는 여러분에게 어떻게 도움이 되었나요?
요약: Go 언어의 미래를 함께 만들어 가기 위해 여러분의 의견을 듣고자 합니다. 설문 조사에 참여하여 여러분의 경험과 피드백을 공유해 주세요.
👉 [자세히 보기](https://go.dev/blog/survey2025-announce)

## 🔹 Helm - Path To Releasing Helm v4
제목: Helm v4 출시 경로

요약: Helm v4의 첫 번째 알파 버전이 출시되었습니다. Helm v4 개발이 막바지에 이르렀기 때문에, 현재 진행 상황과 더 넓은 커뮤니티가 참여할 수 있는 방법에 대한 세부 사항을 공유하고자 합니다.
👉 [자세히 보기](https://helm.sh/blog/path-to-helm-v4/)

