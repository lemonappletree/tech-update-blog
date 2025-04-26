# 🛠️ 2025-04-26 기술 업데이트 요약

## 🔹 Kubernetes - Kubernetes v1.33: User Namespaces enabled by default!
제목: 쿠버네티스 v1.33: 사용자 네임스페이스 기본 활성화!

요약: 쿠버네티스 v1.33에서는 사용자 네임스페이스 지원이 기본적으로 활성화되었습니다. 이는 스택 요구사항이 충족될 경우, 파드가 사용자 네임스페이스를 사용할 수 있음을 의미합니다. 이제 이 기능을 사용하기 위해 쿠버네티스 기능 플래그를 활성화할 필요가 없습니다.

이 블로그 포스트는 사용자 네임스페이스에 대한 일반적인 질문에 답변합니다. 먼저 사용자 네임스페이스의 정의와 중요성을 간략히 정리합니다. 사용자 네임스페이스는 컨테이너의 UID와 GID를 호스트와 분리하여, 컨테이너가 호스트의 UID/GID와 겹치지 않도록 합니다. 이는 횡적 이동 방지, 호스트 격리 강화, 새로운 사용 사례의 활성화라는 세 가지 주요 이점을 제공합니다.

또한, 블로그 포스트에서 사용자 네임스페이스를 활용하여 특정 CVE가 어떻게 완화되는지에 대한 데모도 제공합니다. 사용자 네임스페이스 사용에 대한 요건, 설정 방법, idmap 마운트의 필요성 등 다양한 질문에 대한 답변도 포함되어 있습니다.

사용자 네임스페이스는 루트 권한 없이도 컨테이너 내에서 루트로 실행할 수 있게 하며, 이는 애플리케이션을 변경하지 않고 비루트 사용자로 실행할 수 있도록 해줍니다. 이로 인해 보안이 강화되고 새로운 사용 사례가 가능해집니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/04/25/userns-enabled-by-default/)

## 🔹 Spring Boot - Spring Boot 3.5.0-RC1 available now
제목: Spring Boot 3.5.0-RC1 출시

요약: 팀과 기여한 모든 분들을 대표하여 Spring Boot 3.5.0-RC1이 출시되었음을 기쁘게 발표합니다. 이 버전은 [여기](https://repo.spring.io/milestone)에서 다운로드할 수 있습니다. 이번 릴리스에는 [133개의 개선 사항, 문서 개선, 종속성 업그레이드, 버그 수정](https://github.com/spring-projects/spring-boot/releases/tag/v3.5.0-RC1)이 포함되어 있습니다. 주목할 만한 새로운 기능으로는 Cloud Native Buildpacks 사용 시 Docker의 자격 증명 저장소 및 도우미 지원, 구성 속성 바인딩 성능 개선, 주석 기반 필터 및 서블릿 등록, 빈의 백그라운드 초기화를 위한 자동 구성, 글로벌 WebClient 구성을 위한 속성 등이 있습니다. 자세한 내용과 업그레이드 지침은 [릴리스 노트](https://github.com/spring-projects/spring-boot/wiki/Spring-Boot-3.5.0-RC1-Release-Notes)를 참조하세요. 이슈 보고서와 풀 리퀘스트로 기여해주신 모든 분들께 감사드립니다.

도움이 되고 싶으신 경우, 이슈 리포지토리에서 ["기여에 이상적인" 태그](https://github.com/spring-projects/spring-boot/labels/status%3A%20ideal-for-contribution)를 확인해보세요. 일반적인 질문은 [Stack Overflow](https://stackoverflow.com)에서 [spring-boot 태그](https://stackoverflow.com/tags/spring-boot)를 사용해 질문하실 수 있습니다.

[프로젝트 페이지](https://spring.io/projects/spring-boot) | [GitHub](https://github.com/spring-projects/spring-boot) | [이슈](https://github.com/spring-projects/spring-boot/issues) | [문서](https://docs.spring.io/spring-boot/3.5/) | [Stack Overflow](https://stackoverflow.com/questions/tagged/spring-boot)

링크: [https://spring.io/blog/2025/04/25/spring-boot-3-5-0-RC1-available-now](https://spring.io/blog/2025/04/25/spring-boot-3-5-0-RC1-available-now)
👉 [자세히 보기](https://spring.io/blog/2025/04/25/spring-boot-3-5-0-RC1-available-now)

## 🔹 Docker - How to build and deliver an MCP server for production
제목: 프로덕션용 MCP 서버 구축 및 배포 방법

요약: 2024년 12월, 우리는 Anthropic과 함께 AI 에이전트를 활용한 도구 실행에 대한 완전히 새로운 사양인 모델 컨텍스트 프로토콜(MCP)에 대한 블로그를 게시했습니다. 이후 개발자들이 MCP를 사용하여 에이전틱 AI와 함께 그들의 도구를 구축하고, 공유하며, 실행하려는 욕구가 폭발적으로 증가했습니다. 우리는 새로운 [...]
👉 [자세히 보기](https://www.docker.com/blog/build-to-prod-mcp-servers-with-docker/)

## 🔹 Java - Finalizing the Java On-ramp - Inside Java Newscast #90
제목: Java 온램프의 마무리 - Inside Java Newscast #90  
요약: Java 25 릴리스에서는 큰 변화, 혹은 작고 압축된 변화가 다가오고 있습니다! 이번 Inside Java Newscast 에피소드에서는 Java 25에서 최종 확정될 Paving the On-ramp 기능 세트를 살펴봅니다. 또한, Java를 배우고자 하는 사람들과 Java를 가르치는 사람들을 위한 새로운 웹사이트 lear.java의 출시에 대해서도 다룹니다.
👉 [자세히 보기](https://inside.java/2025/04/24/ijn-ep-90/)

## 🔹 Golang - More predictable benchmarking with testing.B.Loop
제목: 더 예측 가능한 벤치마킹을 위한 testing.B.Loop  
요약: Go 1.24에서 개선된 벤치마크 루프  
링크: https://go.dev/blog/testing-b-loop
👉 [자세히 보기](https://go.dev/blog/testing-b-loop)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
제목: Helm @ KubeCon + CloudNativeCon EU '25  
내용 요약: Helm 팀이 올해도 KubeCon + CloudNativeCon EU '25에 참가하기 위해 영국 런던으로 향합니다. 이번 행사는 4월 1일부터 4일까지 진행됩니다. 올해 말 출시 예정인 Helm 4에 대한 논의에 참여하고 싶다면, 유지보수자들과의 대화 세션 및 Project Pavilion에 있는 Helm 부스를 방문해 보세요. 주간 동안 진행될 모든 Helm 관련 활동에 대한 자세한 내용은 아래를 참조하세요.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

