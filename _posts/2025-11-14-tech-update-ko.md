# 🛠️ 2025-11-14 기술 업데이트 요약

## 🔹 Kubernetes - Ingress NGINX Retirement: What You Need to Know
Kubernetes SIG 네트워크와 보안 대응 위원회는 Ingress NGINX의 은퇴를 발표했습니다. Ingress NGINX는 2026년 3월까지 유지 보수되며 이후에는 더 이상의 릴리스나 버그 수정, 보안 업데이트가 제공되지 않습니다. 현재 Ingress NGINX를 사용하는 배포는 계속 작동하며, 설치 아티팩트도 여전히 사용할 수 있습니다. 사용자는 Gateway API 등 대안으로의 마이그레이션을 권장합니다. Ingress NGINX는 Kubernetes 프로젝트 초기에 개발된 인그레스 컨트롤러로, 높은 유연성과 다양한 기능으로 인기를 끌었습니다. 하지만 유지 보수 인력의 부족과 기술 부채 문제로 프로젝트 유지가 어려워졌습니다. SIG 네트워크와 보안 대응 위원회는 사용자의 안전을 우선시하기 위해 프로젝트 은퇴를 결정했으며, 사용자들은 즉시 마이그레이션을 시작할 것을 권장합니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/11/11/ingress-nginx-retirement/)

## 🔹 Spring Boot - Spring Cloud 2025.1.0-RC1 (aka Oakwood) has been released
2025년 11월 13일, Spring Cloud 2025.1.0-RC1(Oakwood) 릴리스 후보가 공개되었습니다. 이 릴리스는 Spring Milestone 저장소에서 다운로드할 수 있으며, 주요 변경 사항으로는 Spring Boot 4.0.0-RC2 지원, Jackson 3 업데이트, JSpecify Null-Safety 초기 지원, 종속성 업데이트 및 버그 수정 등이 포함되어 있습니다. 더불어, Spring Cloud Function, Spring Cloud Consul, Spring Cloud Gateway, Spring Cloud Commons, Spring Cloud Vault, Spring Cloud Stream, Spring Cloud Config, Spring Cloud Contract, Spring Cloud Kubernetes, Spring Cloud Circuitbreaker 등 다양한 모듈들이 업데이트되었으며, 각 모듈의 변경 사항은 GitHub에서 확인할 수 있습니다. Maven 및 Gradle을 사용하여 프로젝트에 쉽게 통합할 수 있으며, 자세한 정보는 Spring Cloud GitHub, Gitter, Stack Overflow, Twitter에서 확인할 수 있습니다.
👉 [자세히 보기](https://spring.io/blog/2025/11/13/spring-cloud-2025-1-0-RC1-aka-oakwood-has-been-released)

## 🔹 Docker - Cagent Comes to Docker Desktop with Built-In IDE Support through ACP
Docker Desktop에 cagent가 기본적으로 포함되면서, 개발자들이 별도의 설치 과정 없이 AI 에이전트를 구축할 수 있게 되었습니다. cagent는 코드를 작성하는 대신 YAML 구성 파일을 사용하여 AI 에이전트를 구축할 수 있는 Docker의 오픈 소스 도구입니다. 이를 통해 에이전트의 동작과 도구를 정의할 수 있습니다.
👉 [자세히 보기](https://www.docker.com/blog/cagent-comes-to-docker-desktop-with-built-in-ide-support-through-acp/)

## 🔹 Java - JEP targeted to JDK 26: 516: Ahead-of-Time Object Caching with Any GC
제목: JDK 26을 목표로 한 JEP: 516: 모든 GC에서의 사전 객체 캐싱

요약: JDK 26을 목표로 하는 JEP 516은 모든 가비지 컬렉터(GC)와 호환 가능한 사전 객체 캐싱(Ahead-of-Time Object Caching)을 도입하는 것을 목표로 하고 있습니다. 이는 애플리케이션의 시작 시간을 단축하고 성능을 향상시키기 위한 기술입니다.
👉 [자세히 보기](https://inside.java/2025/11/13/jep516-target-jdk26/)

## 🔹 Golang - The Green Tea Garbage Collector
Go 1.25 버전에는 새로운 실험적 가비지 컬렉터인 Green Tea가 포함되었습니다. 이 가비지 컬렉터는 메모리 관리와 성능 최적화를 목표로 하고 있습니다. 자세한 내용은 공식 블로그 링크를 통해 확인할 수 있습니다.
👉 [자세히 보기](https://go.dev/blog/greenteagc)

