# 🛠️ 2025-10-30 기술 업데이트 요약

## 🔹 Kubernetes - 7 Common Kubernetes Pitfalls (and How I Learned to Avoid Them)
이 기술 블로그 글은 Kubernetes를 사용할 때 자주 발생하는 실수와 이를 피하는 방법에 대해 다룹니다. Kubernetes는 강력하지만 때때로 실망스럽기도 하며, 글쓴이는 자신이 겪었던 문제들을 바탕으로 7가지 주요 함정을 설명합니다.

1. **리소스 요청 및 제한 설정 누락**: Pod의 CPU 및 메모리 요구사항을 명시하지 않으면 리소스 부족이나 비정상적인 리소스 사용이 발생할 수 있습니다. 적절한 요청 및 제한 값을 설정하여 이를 방지해야 합니다.

2. **활성 및 준비 상태 검사 과소평가**: 컨테이너가 제대로 작동하는지 확인하는 liveness와 readiness probe를 설정하지 않으면 응답 없는 애플리케이션을 감지하지 못할 수 있습니다.

3. **컨테이너 로그에만 의존**: `kubectl logs` 명령어에만 의존하면 로그 손실이 발생할 수 있습니다. 로그를 중앙에서 관리하여 이 문제를 해결해야 합니다.

4. **개발 환경과 프로덕션 환경의 동일한 처리**: 환경별로 다른 요구 사항을 고려하지 않으면 성능 및 보안 문제가 발생할 수 있습니다. 각 환경에 맞춘 설정을 사용해야 합니다.

5. **오래된 리소스 방치**: 사용하지 않는 리소스를 제거하지 않으면 클러스터 리소스가 낭비되고 비용이 증가할 수 있습니다. 정기적으로 클러스터를 점검하여 불필요한 리소스를 정리해야 합니다.

6. **네트워킹 과도 탐색**: Kubernetes 네이티브 네트워킹을 충분히 이해하지 않고 고급 네트워킹 솔루션을 도입하면 문제 해결이 어려워질 수 있습니다.

7. **보안 및 RBAC 소홀**: 보안 구성이 부실하면 클러스터가 다양한 위험에 노출될 수 있습니다. 엄격한 보안 정책을 적용하여 이를 방지해야 합니다.

Kubernetes는 뛰어난 도구지만 사용자 설정이 필요하며, 이러한 함정을 피하면 많은 문제를 예방할 수 있습니다. 추가 학습을 위해 공식 문서와 커뮤니티를 활용하는 것이 좋습니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/10/20/seven-kubernetes-pitfalls-and-how-to-avoid/)

## 🔹 Spring Boot - Reactive Support in Spring for Apache Pulsar Will Be Discontinued
Spring 팀은 Apache Pulsar를 위한 Spring 프로젝트에서 Reactive 지원을 중단하기로 결정했습니다. 이는 프로젝트의 장기적인 지속 가능성을 고려하여 이루어진 결정으로, 사용률 감소와 다운로드 추세를 기반으로 한 것입니다. 따라서, `spring-pulsar-reactive` 모듈은 Spring for Apache Pulsar 2.0.0부터 모든 향후 릴리스에서 제거될 예정이며, Spring Boot의 관련 지원도 Spring Boot 4.0.0부터 종료됩니다. 그러나 팀은 여전히 Apache Pulsar를 위한 Spring 프로젝트의 지속적인 개발에 전념하고 있으며, 관련 질문이나 우려 사항이 있는 경우 GitHub 저장소나 블로그 댓글을 통해 문의할 수 있습니다.
👉 [자세히 보기](https://spring.io/blog/2025/10/29/spring-pulsar-reactive-discontinued)

## 🔹 Docker - How to add MCP Servers to Claude Desktop with Docker MCP Toolkit
이 블로그 글은 Claude Desktop을 개발 도구와 연결하여 실제 작업을 수행할 수 있는 개발 파트너로 만드는 방법에 대해 설명합니다. Docker MCP Toolkit을 사용하면 로컬 머신에 직접 접근하지 않고도 안전하고 보안적으로 Claude를 활용할 수 있습니다. 이 글에서는 Claude Desktop과 실제 개발 도구를 연결하는 방법에 대한 안내를 제공합니다.
👉 [자세히 보기](https://www.docker.com/blog/connect-mcp-servers-to-claude-desktop-with-mcp-toolkit/)

## 🔹 Java - AI World: Georges Saab Unveils Java 25 for AI and Cloud
블로그 글 요약: "AI World" 행사에서 Georges Saab가 Java 25의 새로운 기능을 발표하며 AI, 기업 현대화, 클라우드 네이티브 개발을 가속화하는 방법을 소개합니다. Oracle AI World 2025의 Oracle TV 세그먼트를 통해 플랫폼의 최신 혁신에 대한 전문가의 통찰을 확인할 수 있습니다.
👉 [자세히 보기](https://inside.java/2025/10/29/aiworld-java-for-ai/)

## 🔹 Golang - The Green Tea Garbage Collector
Go 1.25 버전에는 새로운 실험적 가비지 컬렉터인 Green Tea가 포함되었습니다. 이 새로운 가비지 컬렉터의 도입으로 메모리 관리가 더욱 효율적으로 개선될 것으로 기대됩니다.
👉 [자세히 보기](https://go.dev/blog/greenteagc)

