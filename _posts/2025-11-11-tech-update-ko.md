# 🛠️ 2025-11-11 기술 업데이트 요약

## 🔹 Kubernetes - Announcing the 2025 Steering Committee Election Results
2025년 쿠버네티스 운영위원회 선거 결과가 발표되었습니다. 이번 선거에서는 7명의 위원 중 4명의 자리가 새롭게 선출되었으며, 새로 선출된 위원들은 2년간 임기를 수행하게 됩니다. 이번에 선출된 위원들은 Kat Cosgrove, Paco Xu, Rita Zhang, Maciej Szulik이며, 이들은 기존 위원들과 함께 프로젝트의 운영을 감독하게 됩니다. 선거에 참여해준 모든 분들께 감사드리며, 운영위원회는 쿠버네티스 프로젝트의 전반적인 거버넌스를 담당하고 있습니다. 또한, 운영위원회는 모든 사람에게 열려 있으며, 회의 노트를 통해 진행 상황을 확인하거나 관련 저장소에 이슈를 제기할 수 있습니다. 이전 회의는 YouTube에서 시청할 수 있습니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/11/09/steering-committee-results-2025/)

## 🔹 Spring Boot - LLM Response Evaluation with Spring AI: Building LLM-as-a-Judge Using Recursive Advisors
이 기술 블로그 글은 대형 언어 모델(LLM)의 응답 평가 방법을 다룹니다. 전통적인 평가 지표인 ROUGE와 BLEU는 LLM의 미묘한 응답을 완벽히 평가하기에 부족하므로, LLM 자체를 평가자로 활용하는 'LLM-as-a-Judge' 방법이 제안됩니다. 연구에 따르면, 이 방법은 인간 평가와 최대 85% 일치하며, 이는 인간 간의 일치율(81%)보다 높습니다.

Spring AI의 재귀 어드바이저(Recursive Advisors)를 활용하여 LLM-as-a-Judge 패턴을 구현하는 방법을 설명하며, 이는 AI 시스템이 자동으로 품질을 관리하고 개선할 수 있게 해줍니다. 또한, 두 가지 주요 평가 패턴인 직접 평가(각 응답에 대한 개별 점수 부여)와 쌍 비교(두 응답 중 더 나은 것을 선택)도 설명합니다.

이 글은 Spring AI의 기능을 활용하여 이러한 평가 패턴을 구현하는 방법과, 품질 평가 및 개선을 위해 재귀적 피드백 루프를 사용하는 방법을 다룹니다. 최종적으로, Spring AI의 재귀 어드바이저가 어떻게 자동화된 품질 관리를 가능하게 하고, 인간 개입 없이도 AI 시스템의 품질을 보장할 수 있는지를 설명합니다.
👉 [자세히 보기](https://spring.io/blog/2025/11/10/spring-ai-llm-as-judge-blog-post)

## 🔹 Docker - Help Define the Future of Development – Take the Docker State of Application Development Survey 2025
제목: 개발의 미래 정의에 도움을 주세요 – Docker 애플리케이션 개발 현황 조사 2025에 참여하세요

요약: Docker 애플리케이션 개발 현황 조사가 올해로 네 번째를 맞이했습니다. 20분 정도 시간을 내어 설문에 참여해 주시면, 애플리케이션 개발 커뮤니티를 더 잘 이해하고 지원하는 데 큰 도움이 됩니다. 여러분이 집중하고 있는 분야, 진행 중인 작업, 가장 중요하게 생각하는 부분에 대해 알고 싶습니다. 여러분의 의견과 피드백은 우리의 발전에 큰 도움이 됩니다.
👉 [자세히 보기](https://www.docker.com/blog/state-of-application-development-survey-2025/)

## 🔹 Java - Serialization 2 0: A Marshalling Update!
블로그 글 제목: Serialization 2 0: 마샬링 업데이트!
요약: Java 직렬화가 만들어진 지 거의 30년이 지난 지금, 객체의 외부화에 대한 애플리케이션 요구사항이 크게 변화했습니다. 이 발표에서는 요구사항과 제약 조건이 어떻게 변화했는지를 설명하며, Java 언어의 최근 개선 사항과 더불어 책임 분담을 명확히 함으로써 객체 구조에 대한 프로그래밍적 접근이 훨씬 간단하고 안전해질 수 있음을 보여줍니다. 이를 통해 상태 추출, 버전 관리, 인코딩 및 재구성에서 더 큰 유연성을 제공하고, 다양한 와이어 포맷을 지원할 수 있습니다.
👉 [자세히 보기](https://inside.java/2025/11/10/devoxxbelgium-serialization2-0-marshalling-update/)

## 🔹 Golang - The Green Tea Garbage Collector
Go 1.25 버전에는 새로운 실험적 가비지 컬렉터인 Green Tea가 포함되었습니다. 이 글에서는 Green Tea의 특징과 작동 방식에 대해 설명하고 있습니다. Green Tea는 메모리 관리 효율성을 높이고, 성능을 향상시키는 것을 목표로 합니다. 이 새로운 가비지 컬렉터는 개발자들에게 향상된 메모리 관리 옵션을 제공할 것으로 기대됩니다.
👉 [자세히 보기](https://go.dev/blog/greenteagc)

