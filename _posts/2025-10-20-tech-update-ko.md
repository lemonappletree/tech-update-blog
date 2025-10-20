# 🛠️ 2025-10-20 기술 업데이트 요약

## 🔹 Kubernetes - Spotlight on Policy Working Group
이 기술 블로그 글은 Kubernetes의 정책 작업 그룹(Policy Working Group)에 대한 내용을 다루고 있습니다. 이 그룹은 Kubernetes 클러스터의 정책 개발, 구현 및 표준화를 목적으로 활동했으며, 그들의 임무는 완료되어 현재는 활동하지 않습니다. Kubernetes의 복잡한 정책 환경을 명확하고 일관되게 유지하기 위해 협업 방식으로 작업했으며, 정책 아키텍처를 개발하여 개발자와 사용자 모두에게 혜택을 주고자 했습니다.

글에서는 전 공동 의장인 Jim Bugwadia, Andy Suderman, Poonam Lamba와의 인터뷰를 통해 정책 작업 그룹의 역할과 활동에 대해 심도 있게 설명합니다. 정책 작업 그룹은 Kubernetes의 정책 정의 및 구현 표준화를 연구하고, Kubernetes 정책 보고서 API와 같은 여러 프로젝트를 추진했으며, 커뮤니티에 정책 관리에 대한 모범 사례를 교육하는 데 목표를 두었습니다.

작업 그룹은 Kubernetes SIG Auth 및 SIG Security와 긴밀히 협력했으며, Kubernetes 정책 보고서 API 표준화를 주요 업적으로 달성했습니다. 또한, Kubernetes의 다양한 정책 관련 프로젝트에 기여했으며, 정책 관리 솔루션의 적절한 사용 패턴에 대한 커뮤니티 교육도 진행했습니다.

작업 그룹은 시간 부족 및 합의 기반 모델로 인해 느린 의사 결정 과정과 같은 여러 도전 과제를 겪었지만, 다양한 의견을 존중하며 협력적인 환경을 유지하려고 노력했습니다. Kubernetes 커뮤니티는 초보자에게도 친숙하며, 참여를 권장하고 있습니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/10/18/wg-policy-spotlight-2025/)

## 🔹 Spring Boot - Spring Data 2025.1.0-RC1 released
이 블로그 글은 Spring Data의 다음 세대에 대한 첫 번째 릴리스 후보(RC) 버전인 2025.1.0-RC1의 출시를 발표하는 내용입니다. 이번 RC 버전은 다양한 새로운 기능의 개선과 버그 수정, 의존성 업그레이드를 포함하고 있습니다. 사용자들에게 새로운 기능을 시도해보고 피드백을 제공해 줄 것을 요청하고 있습니다. 이 릴리스에는 Spring Data Commons, JPA, MongoDB, Neo4j, KeyValue, Apache Cassandra, LDAP, REST, Redis, Elasticsearch, Couchbase, Relational 등이 포함되어 있으며, 각각의 Javadoc, 문서 및 변경 로그에 대한 링크가 제공됩니다.
👉 [자세히 보기](https://spring.io/blog/2025/10/17/spring-data-2025-1-0-RC1-released)

## 🔹 Docker - How to add MCP Servers to OpenAI’s Codex with Docker MCP Toolkit
이 기술 블로그 글은 Docker MCP Toolkit을 사용하여 OpenAI의 Codex를 MCP 서버에 추가하는 방법에 대해 설명합니다. AI 비서가 코드를 작성하는 방식을 혁신하고 있지만, 전문적이고 정밀한 도구와 상호작용할 때 그 진정한 잠재력이 발휘됩니다. OpenAI의 Codex는 뛰어난 코딩 파트너이지만, 이를 실행 중인 인프라와 직접 연결하면 어떤 일이 벌어질까요? 여기서 Docker MCP Toolkit이 등장합니다. Model Context Protocol (MCP) Toolkit은... (요약은 블로그의 링크를 통해 원문을 참조하여 더 자세히 확인할 수 있습니다.)
👉 [자세히 보기](https://www.docker.com/blog/connect-codex-to-mcp-servers-mcp-toolkit/)

## 🔹 Java - From JDK 21 to JDK 25 - Java Performance Update 2025
블로그 글은 JDK 21에서 JDK 25로의 성능 향상에 대해 다루고 있습니다. JDK 25가 새로 출시되면서 JDK 21에 비해 성능이 크게 개선되었으며, 애플리케이션 코드를 변경하지 않고도 더 빠르게 실행할 수 있게 되었습니다. 글에서는 표준 Java 라이브러리, JIT 컴파일러, 가비지 컬렉터를 포함한 13가지 구체적인 성능 개선 사항을 살펴봅니다. 특히, 'Stable Value'라는 새로운 프리뷰 기능이 도입되어, 가변 필드와 불변 필드의 장점을 동시에 활용할 수 있게 되었습니다. 이 기능이 어떻게 작동하는지, 성능이 얼마나 개선될 수 있는지, 그리고 개발자가 어떻게 이를 활용할 수 있는지를 설명합니다. 또한, 설계상의 고려 사항, 개발자 피드백의 중요성, 그리고 상반된 최적화 기준과 다양한 플랫폼 특성 속에서 JDK 엔지니어들이 성능을 평가하는 방법에 대해서도 탐구합니다.
👉 [자세히 보기](https://inside.java/2025/10/18/devoxxbelgium-java-performance-update/)

## 🔹 Golang - Flight Recorder in Go 1.25
Go 1.25 버전에서는 새로운 진단 도구로 '플라이트 레코딩' 기능이 도입되었습니다. 이 기능은 프로그램의 실행을 기록하고 분석하는 데 도움을 주는 도구입니다. 개발자는 이를 통해 실행 중인 프로그램의 상태를 더 잘 이해하고, 문제를 진단하는 데 유용하게 활용할 수 있습니다.
👉 [자세히 보기](https://go.dev/blog/flight-recorder)

## 🔹 Helm - Helm Turns 10
블로그 글 "Helm Turns 10"은 Helm의 10주년을 기념하는 내용입니다. Helm은 10년 전 Kubernetes 1.1.0의 출시 직후 해커톤에서 탄생했습니다. 최초 커밋은 Helm v1의 코드베이스가 있는 helm-classic Git 저장소에서 확인할 수 있습니다. 초기 Helm은 Deployment Manager와 합병되기 전, 그리고 Kubernetes 프로젝트에 통합되기 전의 버전입니다.
👉 [자세히 보기](https://helm.sh/blog/helm-turns-ten/)

