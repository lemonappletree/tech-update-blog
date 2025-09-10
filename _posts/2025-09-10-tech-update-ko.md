# 🛠️ 2025-09-10 기술 업데이트 요약

## 🔹 Kubernetes - Kubernetes v1.34: Snapshottable API server cache
이 블로그 글은 Kubernetes v1.34에서 도입된 새로운 기능인 '스냅샷 가능 API 서버 캐시'에 대해 설명하고 있습니다. 이 기능은 API 서버의 성능과 안정성을 개선하기 위한 오랜 기간의 노력의 결실로, 특히 메모리 사용량을 줄이고 etcd 데이터 저장소의 부하를 줄이는 데 중점을 두었습니다. 이전 릴리스에서는 캐시를 통한 일관된 읽기와 대용량 응답 스트리밍을 도입하여 성능을 개선했지만, 역사적인 리스트 요청 시 발생하는 예측 불가능한 메모리 사용 문제는 여전히 남아 있었습니다. 이번 v1.34에서는 이러한 문제를 해결하기 위해 캐시가 특정 시점의 상태를 효율적으로 스냅샷할 수 있도록 개선되었습니다. 이를 통해 거의 모든 읽기 요청이 API 서버의 메모리에서 직접 처리될 수 있게 되어, 클러스터의 안정성과 확장성이 크게 향상되었습니다. 이 기능은 기본적으로 활성화되어 있어, 사용자는 별도의 조치 없이도 이러한 성능 및 안정성 개선의 혜택을 받을 수 있습니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/09/09/kubernetes-v1-34-snapshottable-api-server-cache/)

## 🔹 Spring Boot - Access API Moves to Spring Security Access
이 블로그 글은 Spring Security가 5년 전부터 권한 부여 API를 현대화하기 시작했음을 설명합니다. 이 과정에서 Authorized POJOs, 값 마스킹, 다중 요인 인증 등 다양한 기능이 추가되었습니다. 기존 Access API는 대부분 사용 중단되었으며, 이는 AccessDecisionManager, AccessDecisionVoter, FilterSecurityInterceptor 같은 구성 요소들을 포함합니다. Spring Security 7.0.0-M3에서는 이러한 사용 중단된 API를 포함한 새로운 모듈 spring-security-access가 도입되어, 이전 API를 사용하는 조직들이 최신 버전으로 업데이트하도록 유도합니다. 이 모듈은 선택적 의존성으로, 기존의 AuthorizationManager를 사용하는 경우에는 변경이 필요 없습니다.
👉 [자세히 보기](https://spring.io/blog/2025/09/09/access-api-moves-to-spring-security-access)

## 🔹 Docker - Docker Acquisition of MCP Defender Helps Meet Challenges of Securing the Agentic Future
Docker, Inc.가 AI 애플리케이션 보안을 전문으로 하는 MCP Defender를 인수했다고 발표했습니다. AI 기술의 급속한 발전은 소프트웨어 개발에 큰 변화를 가져왔으며, 이에 따라 새로운 보안 문제도 대두되고 있습니다. Docker는 이번 인수를 통해 클라우드 및 AI 기반 개발 도구와 서비스를 강화하고, AI의 발전에 따른 보안 문제를 해결할 계획입니다.
👉 [자세히 보기](https://www.docker.com/blog/docker-acquires-mcp-defender-ai-agent-security/)

## 🔹 Java - All API Additions From Java 21 to 25 #RoadTo25
이 기술 블로그 글은 Java 21부터 Java 25까지의 모든 API 추가 사항을 다루고 있습니다. 주요 추가 기능으로는 스코프 값, 스트림 수집기, 클래스 파일 API, 외부 함수 및 메모리 API, Javadoc 추가가 포함됩니다. 이를 통해 새로운 Java 버전의 주요 변경 사항과 기능을 이해할 수 있습니다.
👉 [자세히 보기](https://inside.java/2025/09/09/roadto25-api/)

## 🔹 Golang - A new experimental Go API for JSON
Go 1.25 버전에서 새로운 실험적 JSON API가 도입되었습니다. 이번 업데이트는 `encoding/json/jsontext`와 `encoding/json/v2` 패키지에 대한 지원을 제공합니다. 이는 Go 언어에서 JSON 처리 기능을 확장하려는 시도로 볼 수 있습니다.
👉 [자세히 보기](https://go.dev/blog/jsonv2-exp)

## 🔹 Helm - Path To Releasing Helm v4
제목: Helm v4 출시 경로

요약: Helm v4의 첫 번째 알파 버전이 출시되었습니다. Helm v4 개발이 막바지에 이르렀으며, 현재 진행 상황과 더 넓은 커뮤니티가 어떻게 참여할 수 있는지에 대한 세부 사항을 공유하고자 합니다.
👉 [자세히 보기](https://helm.sh/blog/path-to-helm-v4/)

