# 🛠️ 2025-11-12 기술 업데이트 요약

## 🔹 Kubernetes - Announcing the 2025 Steering Committee Election Results
2025년 쿠버네티스 운영위원회 선거 결과가 발표되었습니다. 운영위원회는 총 7개의 자리를 가지고 있으며, 이번 선거에서는 4개의 자리가 새롭게 선출되었습니다. 운영위원회는 쿠버네티스 프로젝트의 거버넌스를 감독하며, 모든 구성원은 커뮤니티에 의해 선출됩니다. 이번에 선출된 위원들은 Kat Cosgrove, Paco Xu, Rita Zhang, Maciej Szulik이며, 이들은 기존의 Antonio Ojea, Benjamin Elder, Sascha Grunert와 함께 활동합니다. 이번 선거를 성공적으로 이끌어준 선거 담당자들과 퇴임하는 위원들에게 감사의 인사를 전하며, 운영위원회는 모든 사람에게 열려 있으며, 관련 회의에 참여하거나 의견을 제시할 수 있습니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/11/09/steering-committee-results-2025/)

## 🔹 Spring Boot - LLM Response Evaluation with Spring AI: Building LLM-as-a-Judge Using Recursive Advisors
이 블로그 글은 AI 시스템의 품질 평가를 자동화하기 위해 대형 언어 모델(LLM)을 심판으로 사용하는 방법에 대해 설명합니다. 전통적인 평가 지표(ROUGE, BLEU 등)는 LLM의 복잡한 응답을 평가하는 데 한계가 있으며, 인간 평가자는 정확하지만 비용이 많이 들고 느리다는 문제가 있습니다. 이에 대한 해결책으로 LLM-as-a-Judge 접근법이 제시되는데, LLM 자체가 생성된 콘텐츠의 품질을 평가하여 인간의 판단과 최대 85% 일치하는 결과를 보여줍니다. Spring AI의 Recursive Advisors는 이러한 평가 패턴을 구현할 수 있는 우아한 프레임워크를 제공합니다. 이를 통해 자동화된 품질 관리를 통해 AI 시스템의 자가 개선을 가능하게 합니다. 이 글은 LLM-as-a-Judge의 평가 패턴, 적절한 모델 선택, 그리고 Spring AI를 활용한 구현 예제를 포함하고 있습니다. 주요 이점으로는 자동화된 품질 관리와 편향 완화가 있으며, 이는 챗봇, 콘텐츠 생성 및 복잡한 AI 워크플로우 전반에 걸쳐 신뢰할 수 있는 품질 보증을 제공합니다.
👉 [자세히 보기](https://spring.io/blog/2025/11/10/spring-ai-llm-as-judge-blog-post)

## 🔹 Docker - Docker Engine v29: Foundational Updates for the Future
블로그 글 "Docker Engine v29: Foundational Updates for the Future"는 주로 리눅스 사용자들을 위한 내용으로, Docker Engine(커뮤니티 에디션)을 직접 호스트에서 실행하는 경우에 해당합니다. Docker Desktop 사용자는 별도의 조치를 취할 필요가 없으며, 향후 Desktop 릴리스에 자동으로 엔진 업데이트가 포함됩니다. Docker Engine v29는 Docker 플랫폼의 미래를 위해 기초를 다지는 릴리스로, 향후 발전을 위한 중요한 기반을 마련하고 있습니다.
👉 [자세히 보기](https://www.docker.com/blog/docker-engine-version-29/)

## 🔹 Java - Serialization 2 0: A Marshalling Update!
이 블로그 글은 Java Serialization의 업데이트에 대해 설명합니다. Java Serialization은 세간에 부정적으로 여겨지는 기능으로, 처음 생성된 지 거의 30년이 지났습니다. 그동안 객체의 외부화에 대한 애플리케이션 요구사항이 크게 변화했습니다. 이 프레젠테이션은 이러한 요구사항과 제약사항이 어떻게 변했는지를 설명하고, Java 언어의 최근 개선 사항과 책임 분담의 단순화 및 명확화를 통해 객체 구조에 대한 프로그래밍적 사고가 어떻게 더 간단하고 안전한 모델로 발전할 수 있는지를 보여줍니다. 이로 인해 상태 추출, 버전 관리, 인코딩 및 재구성에서 더 큰 유연성을 제공하고, 다양한 전송 형식을 지원할 수 있습니다.
👉 [자세히 보기](https://inside.java/2025/11/10/devoxxbelgium-serialization2-0-marshalling-update/)

## 🔹 Golang - The Green Tea Garbage Collector
Go 1.25 버전에는 새로운 실험적 가비지 컬렉터인 Green Tea가 포함되어 있습니다. 이 가비지 컬렉터는 메모리 관리 효율성을 높이기 위해 개발되었습니다.
👉 [자세히 보기](https://go.dev/blog/greenteagc)

