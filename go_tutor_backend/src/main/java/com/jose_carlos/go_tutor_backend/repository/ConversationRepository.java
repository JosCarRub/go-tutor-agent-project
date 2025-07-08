package com.jose_carlos.go_tutor_backend.repository;

import com.jose_carlos.go_tutor_backend.entities.Conversation;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

import java.time.LocalDateTime;
import java.util.List;

@Repository
public interface ConversationRepository extends MongoRepository<Conversation,String> {

    List<Conversation> findByCreatedAtBetween(LocalDateTime startDate, LocalDateTime endDate);

}
