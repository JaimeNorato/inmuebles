-- Creacion de tabla pivot para almacenar los favoritos de un usuario
CREATE TABLE property_favorites_user(
    user_id int(8) NOT NULL,
    property_id int(11) NOT NULL,
    PRIMARY KEY (user_id,property_id),
    UNIQUE KEY property_favorites_user_user_id_property_id_uniq(user_id,property_id),
    CONSTRAINT property_favorites_user_user_id_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id),
    CONSTRAINT property_favorites_user_property_id_fk_property_id FOREIGN KEY (property_id) REFERENCES property(id)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- consulta para obtener los favoritos de un usuario
SELECT fv.user_id, u.first_name, u.last_name, fv.property_id, p.address,p.city,p.price
FROM property_favorites_user fv
JOIN auth_user u on fv.user_id=u.id
JOIN property p on fv.user_id=p.id
WHERE fv.user_id=1;