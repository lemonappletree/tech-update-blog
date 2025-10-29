# 🛠️ 2025-10-29 기술 업데이트 요약

## 🔹 Kubernetes - 7 Common Kubernetes Pitfalls (and How I Learned to Avoid Them)
이 기술 블로그 글은 Kubernetes 사용 시 흔히 겪을 수 있는 7가지 함정과 이를 피하는 방법을 다루고 있습니다. 처음 Kubernetes를 사용할 때 저자는 여러 실수를 경험했으며, 이를 바탕으로 유용한 팁들을 공유합니다.

1. **자원 요청 및 제한 생략**: Pod 명세에 CPU 및 메모리 요구사항을 명시하지 않는 실수를 피하려면 적절한 자원 요청 및 제한을 설정해야 합니다.
   
2. **활성화 및 준비 프로브 과소평가**: 컨테이너의 상태를 확인할 수 있도록 활성화 및 준비 프로브를 설정하는 것이 중요합니다.

3. **컨테이너 로그에만 의존**: 로그를 중앙 집중화하고 Prometheus 같은 도구와 결합하여 로그 손실을 방지하는 것이 좋습니다.

4. **개발과 운영 환경 동일하게 취급**: 환경별로 커스터마이징된 설정이 필요하며, 이를 위해 Kustomize와 같은 도구를 사용할 수 있습니다.

5. **오래된 리소스 방치**: 정기적으로 클러스터를 감사하고 불필요한 리소스를 제거하여 클러스터 자원을 효율적으로 관리합니다.

6. **네트워킹에 너무 빨리 깊이 들어감**: Kubernetes 기본 네트워킹을 이해한 후에 고급 네트워킹 솔루션을 도입해야 합니다.

7. **보안 및 RBAC 소홀**: RBAC를 활용해 역할과 권한을 정의하고, 최신 보안 모범 사례를 따르는 것이 필수적입니다.

저자는 Kubernetes 사용 시 이러한 함정을 피함으로써 불필요한 스트레스와 시간을 절약할 수 있다고 조언합니다. 추가로 Kubernetes 공식 문서와 커뮤니티를 통해 더 깊이 있는 학습을 권장합니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/10/20/seven-kubernetes-pitfalls-and-how-to-avoid/)

## 🔹 Spring Boot - Introducing Spring AI Agents and Spring AI Bench
이 블로그 글은 Spring AI Community GitHub 조직의 새로운 프로젝트인 Spring AI Agents와 Spring AI Bench를 소개합니다. 이 두 프로젝트는 기업 Java 개발 및 일반 소프트웨어 개발 생명 주기(SDLC) 작업을 위한 에이전트 기반 코딩 도구의 사용을 중점적으로 다룹니다. Spring AI Agents는 에이전트 도구를 사용할 수 있는 일관된 인터페이스를 제공하는 AgentClient를 정의합니다. 이와 함께 목표, 컨텍스트, 도구, 평가자, 샌드박스 등의 추상화를 제공하여 효과적인 결과를 도출할 수 있습니다. Spring AI Bench는 에이전트의 목표 지향 기업 워크플로를 평가하는 벤치마크 모음입니다. 이 프로젝트들은 AI 기반 코딩 에이전트의 효과적인 사용을 도모하며, 현재는 Spring AI Community에서 인큐베이팅 중입니다.
👉 [자세히 보기](https://spring.io/blog/2025/10/28/agents-and-benchmarks)

## 🔹 Docker - How to add MCP Servers to Claude Desktop with Docker MCP Toolkit
이 기술 블로그 글은 Claude Desktop을 개발 도구로 활용하기 위한 방법을 설명합니다. Claude를 단순한 대화형 비서에서 실제 작업을 수행할 수 있는 개발 파트너로 변신시키려면 Docker MCP Toolkit을 활용하여 MCP 서버를 Claude Desktop에 연결하는 것이 중요하다고 강조합니다. 이를 통해 로컬 머신에 직접 접속하지 않고도 안전하고 보안적으로 작업을 수행할 수 있습니다. 이 글은 Docker MCP Toolkit이 Claude Desktop과 실제 개발 도구를 연결하는 데 필요한 '빠진 조각'임을 설명합니다.
👉 [자세히 보기](https://www.docker.com/blog/connect-mcp-servers-to-claude-desktop-with-mcp-toolkit/)

## 🔹 Java - JEP targeted to JDK 26: 504: Remove the Applet API
제목: JDK 26을 목표로 한 JEP: 504: Applet API 제거  
요약: JDK 26 버전을 목표로 한 JEP 504는 Applet API를 제거하는 내용을 담고 있습니다.  
링크: [자세한 내용 보기](https://inside.java/2025/10/28/jep504-target-jdk26/)
👉 [자세히 보기](https://inside.java/2025/10/28/jep504-target-jdk26/)

## 🔹 Golang - Flight Recorder in Go 1.25
Go 1.25 버전에서는 새로운 진단 도구인 플라이트 레코딩 기능이 도입되었습니다. 이 도구는 프로그램 실행 중 발생하는 다양한 이벤트를 기록하여 디버깅과 성능 분석에 도움을 줍니다. 플라이트 레코더는 개발자가 애플리케이션의 상태를 더 잘 이해하고 문제를 신속하게 해결할 수 있도록 지원합니다.
👉 [자세히 보기](https://go.dev/blog/flight-recorder)

## 🔹 Helm - Helm Turns 10
블로그 글 "Helm Turns 10"은 Helm의 10주년을 기념하는 내용을 담고 있습니다. Helm은 10년 전 Kubernetes 1.1.0이 출시된 직후 해커톤에서 처음 탄생했습니다. 초기 Helm의 첫 커밋은 GitHub의 helm-classic 저장소에서 확인할 수 있으며, 이는 Deployment Manager와 통합되기 전 Kubernetes 프로젝트에 포함되기 전의 원래 Helm 코드베이스입니다.
👉 [자세히 보기](https://helm.sh/blog/helm-turns-ten/)

