# 🛠️ 2025-05-01 기술 업데이트 요약

## 🔹 Kubernetes - Kubernetes v1.33: Storage Capacity Scoring of Nodes for Dynamic Provisioning (alpha)
Kubernetes v1.33에서는 새로운 알파 기능인 `StorageCapacityScoring`을 도입했습니다. 이 기능은 파드 스케줄링 시 노드의 저장 용량을 고려한 점수 매기기 방법을 추가합니다. 이를 통해 가장 많은 또는 가장 적은 저장 용량이 있는 노드에 파드를 배치할 수 있습니다. 이 기능은 노드 로컬 PV를 프로비저닝할 때 유용하며, 클라우드 환경에서 운영 비용을 줄이기 위해 저장 용량이 가장 적은 노드를 선택하는 데 도움을 줍니다. 기본적으로 이 기능은 비활성화되어 있으며, 사용하려면 `kube-scheduler`의 `--feature-gates` 옵션에 `StorageCapacityScoring=true`를 추가해야 합니다. 기존의 `VolumeCapacityPriority` 기능은 이 새로운 기능으로 대체될 예정입니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/04/30/kubernetes-v1-33-storage-capacity-scoring-feature/)

## 🔹 Spring Boot - Spring AI 1.0.0 M8 Released
Spring AI 1.0.0 M8 버전이 출시되었습니다. 이번 릴리스는 API 설계와 이전 버전의 사용 중단된 기능을 검토한 결과, RC1 릴리스에서의 주요 변화가 개발자들에게 충격을 줄 수 있다는 점을 고려하여 추가적인 마일스톤을 도입했습니다. 개발자들이 RC1 릴리스로 원활하게 업그레이드할 수 있도록, 이번 M8 릴리스에서는 사용 중단된 API와 그 대체 기능이 함께 제공됩니다.

이번 릴리스의 주요 변경 사항은 다음과 같습니다:

1. **채팅 메모리 개선**: 대화 기록 관리를 위한 유연한 `ChatMemory` API와 다양한 저장소 전략을 지원하는 `ChatMemoryRepository` 인터페이스가 추가되었습니다. 

2. **템플릿 렌더링**: 일관된 인터페이스를 제공하는 `TemplateRenderer` API가 도입되어 다양한 템플릿 엔진과의 통합을 지원합니다.

3. **MCP 개선**: MCP 클라이언트 속성에 도구 콜백 구성이 추가되었으며, 서버에서의 완성 사양 및 지침 지원이 향상되었습니다.

4. **프롬프트 엔지니어링 패턴**: 고급 프롬프트 설계를 위한 포괄적인 문서가 추가되었습니다.

5. **벡터 저장소 개선**: Cosmos DB에 대한 Azure Entra ID 인증이 추가되었으며, Cassandra 벡터 저장소의 메시지 순서 및 오류 메시지가 개선되었습니다.

중요한 사용 중단 사항에는 `ChatClient` API의 변경, 프롬프트 템플릿 및 어드바이저 관련 클래스의 사용 중단이 포함됩니다. 

기여자들에 의해 다양한 리팩토링, 버그 수정 및 문서 개선이 이루어졌습니다.
👉 [자세히 보기](https://spring.io/blog/2025/04/30/spring-ai-1-0-0-m8-released)

## 🔹 Docker - Update on the Docker DX extension for VS Code
블로그 글 요약: 이 글에서는 VS Code의 Docker DX 확장의 최신 업데이트 내용을 다룹니다. 새로운 기능들이 추가되어 컨테이너 워크플로우를 개선하고, 작성 작업을 보다 쉽게 할 수 있도록 지원합니다. 앞으로 추가될 예정인 기능들에 대한 정보도 포함되어 있어 Docker 사용자들이 더욱 효율적으로 작업할 수 있도록 돕습니다.
👉 [자세히 보기](https://www.docker.com/blog/docker-dx-extension-for-vs-code-update/)

## 🔹 Java - Announcing Jipher: Java Cryptographic Service Provider for FIPS Environments
Oracle에서 FIPS 환경을 위한 Java 암호화 서비스 제공자인 Jipher를 출시했습니다. Jipher는 FIPS 140-2 인증을 받은 OpenSSL 암호화 모듈을 포함하고 있으며, Java 암호화 아키텍처(JCA) 프레임워크를 사용하는 Java 개발자들이 이를 활용할 수 있도록 합니다.
👉 [자세히 보기](https://inside.java/2025/04/30/jipher-release/)

## 🔹 Golang - More predictable benchmarking with testing.B.Loop
블로그 글은 Go 1.24 버전에서 도입된 `testing.B.Loop` 기능을 통해 벤치마크 테스트를 더 예측 가능하게 수행하는 방법에 대해 설명합니다. 이는 반복 실행 방식을 개선하여 보다 일관된 성능 측정이 가능하도록 합니다. 이로 인해 개발자는 코드의 성능을 더 정확하게 평가할 수 있습니다.
👉 [자세히 보기](https://go.dev/blog/testing-b-loop)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
제목: Helm @ KubeCon + CloudNativeCon EU '25

Helm 팀은 2025년 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU '25에 참가합니다. 올해 말 출시 예정인 Helm 4에 대한 논의에 참여하고, 유지 관리자들과의 대화 세션 및 프로젝트 파빌리온의 Helm 부스에서 더 많은 정보를 확인할 수 있습니다. 주간 동안의 모든 Helm 관련 활동에 대한 자세한 내용은 링크에서 확인할 수 있습니다.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

