# 🛠️ 2025-05-27 기술 업데이트 요약

## 🔹 Kubernetes - Kubernetes v1.33: In-Place Pod Resize Graduated to Beta
이 기술 블로그 글에서는 Kubernetes 프로젝트의 일환으로 v1.33 버전에서 "in-place Pod resize" 기능이 베타 단계로 승격되었음을 발표하고 있습니다. 이 기능은 처음 v1.27에서 알파로 도입되었으며, 이제 기본적으로 활성화됩니다. "in-place Pod resize"는 실행 중인 Pod의 CPU 및 메모리 자원을 재시작 없이 변경할 수 있게 하여, 애플리케이션의 리소스 관리가 더욱 유연하고 덜 방해적이게 합니다. 특히 상태가 있는 애플리케이션, 배치 작업 등에서 유용하며, 리소스 사용 효율성을 높이고 확장 속도를 빠르게 합니다. 알파에서 베타로 발전하면서 사용자 경험과 안정성이 향상되었습니다. 이 기능은 이제 더 넓은 사용을 위해 준비되었으며, 사용자 피드백을 통해 추가 개선이 이루어질 예정입니다. 자세한 사용법과 예시는 공식 Kubernetes 문서를 참조하십시오.
👉 [자세히 보기](https://kubernetes.io/blog/2025/05/16/kubernetes-v1-33-in-place-pod-resize-beta/)

## 🔹 Spring Boot - Repository Vector Search Methods
이 기술 블로그 글은 벡터 검색 방법을 설명하며, 특히 스프링(Sprint) 생태계에서의 벡터 검색의 역할을 다룹니다. 최근 대형 언어 모델(LLM)의 출현으로 생성적 AI가 발전하면서, 데이터의 의미를 고차원 공간에서 벡터로 표현하는 임베딩(embedding)이 주목받고 있습니다. 벡터 검색은 이러한 벡터 표현을 사용해 유사한 항목을 효율적으로 검색하는 방법으로, RAG(Retrieval-augmented generation) 시스템 구축에 주로 활용됩니다.

벡터 검색을 지원하는 데이터베이스는 크게 두 가지로 나뉩니다: 전용 벡터 데이터베이스와 벡터 검색 기능을 포함한 기존 데이터베이스 엔진입니다. 전용 벡터 데이터베이스는 유사 항목 검색에 최적화되어 있으며, Pinecone, Weaviate, Milvus, Qdrant 같은 예시가 있습니다. 반면, Postgres, Oracle, MongoDB 등의 기존 데이터베이스 엔진은 벡터 검색 기능을 추가하여 다양한 데이터 유형과 쿼리를 처리할 수 있습니다.

스프링 AI와 스프링 데이터의 벡터 검색 기능은 AI 기능을 스프링 애플리케이션에 통합하고, 일관된 프로그래밍 모델과 추상화를 제공하여 AI 기반 애플리케이션 개발을 단순화하는 것을 목표로 합니다. 스프링 데이터는 데이터 접근과 관리를 단순화하여 다양한 데이터 소스를 일관되게 사용할 수 있도록 돕습니다.

스프링 데이터 3.5에서는 벡터 데이터 타입이 도입되었고, 스프링 데이터 4.0에서는 JPA, MongoDB, Apache Cassandra를 위한 벡터 검색 메서드가 미리보기 기능으로 제공됩니다. 이러한 벡터 검색 메서드는 검색 결과를 도메인 객체 리스트 대신 검색 결과 리스트로 반환하여, 도메인 모델과는 다른 검색 결과 표현을 제공합니다.
👉 [자세히 보기](https://spring.io/blog/2025/05/23/vector-search-methods)

## 🔹 Docker - Introducing Docker Hardened Images: Secure, Minimal, and Ready for Production
이 블로그 글은 Docker의 새로운 보안 강화 이미지(Docker Hardened Images)에 대해 소개합니다. Docker는 처음부터 개발자들이 소프트웨어를 효율적이고 안전하게 구축, 공유, 실행할 수 있도록 지원해왔습니다. 오늘날 Docker Hub는 매달 140억 회 이상의 이미지 다운로드가 이루어질 만큼 글로벌 소프트웨어 배포의 중심에 있으며, 이를 통해 현대 소프트웨어가 어떻게 구축되는지에 대한 독특한 통찰력을 제공합니다. 이 글에서는 이러한 Docker Hardened Images가 어떻게 보안성과 최소화를 통해 프로덕션 환경에 준비된 상태로 제공되는지 설명하고 있습니다.
👉 [자세히 보기](https://www.docker.com/blog/introducing-docker-hardened-images/)

## 🔹 Java - JEP 510: Key Derivation Function API
블로그 글의 제목은 "JEP 510: Key Derivation Function API"이며, 이는 JDK 25를 목표로 하고 있습니다. 이 JEP는 키 파생 함수(API)에 대한 내용을 다루고 있으며, API의 구현 및 활용에 관한 상세한 정보를 제공할 것으로 보입니다. 해당 글은 JDK의 보안 기능을 강화하고자 하는 개발자들에게 유용할 것입니다.
👉 [자세히 보기](https://inside.java/2025/05/26/jep510-target-jdk25/)

## 🔹 Golang - Go Cryptography Security Audit
제목: Go 암호화 보안 감사

요약: Go의 암호화 라이브러리가 Trail of Bits에 의해 감사를 받았습니다.
👉 [자세히 보기](https://go.dev/blog/tob-crypto-audit)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
블로그 글 요약: Helm 팀이 2025년 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU에 참가합니다. 올해 말 출시 예정인 Helm 4에 대한 논의에 참여할 수 있는 기회로, 발표 세션 및 프로젝트 파빌리온 내 Helm 부스를 방문하여 유지 관리자들과 소통할 수 있습니다. 주간 행사에 대한 자세한 내용은 블로그를 참고하세요.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

